from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.currency import currency_keyboard
from services.currency_service import get_rates
from keyboards.menu import menu_keyboard
from services.history_service import save_history

router = Router()

class ConvertState(StatesGroup):
    waiting_amount = State()
    waiting_target_currency = State()

@router.message(F.text == "💱 Конвертация валют")
async def convert_handler(message: Message, state: FSMContext):
    await state.set_state(ConvertState.waiting_amount)

    await message.answer(
        "💱 Конвертация валют\n\n"
        "Введите сумму и валюту."
    )

@router.message(ConvertState.waiting_amount)
async def process_convert(message: Message, state: FSMContext):
    text = message.text
    data = text.split()

    try:
        amount = float(data[0])
        currency = data[1].upper()

    except (ValueError, IndexError):
        await message.answer(
            "❌ Неверный формат!\n\n"
            "Введите сумму и валюту.\n"
        )
        return

    rates = {
        "USD": 1,
        "EUR": 0.86,
        "RUB": 78.5,
        "TJS": 9.4
    }

    if currency not in rates:
        await message.answer(
            "❌ Такая валюта не поддерживается.\n\n"
            "Доступные валюты:\n"
            "USD\nEUR\nRUB\nTJS"
        )
        return

    await state.update_data(
        amount=amount,
        from_currency=currency
    )

    await state.set_state(ConvertState.waiting_target_currency)

    await message.answer(
        "💱 Выберите валюту, в которую хотите перевести:",
        reply_markup=currency_keyboard
    )


@router.message(ConvertState.waiting_target_currency)
async def choose_currency(message: Message, state: FSMContext):
    data = await state.get_data()

    amount = data["amount"]
    from_currency = data["from_currency"]

    to_currency = message.text.split()[-1]

    data = get_rates()
    rates = data["rates"]

    from_rate = rates[from_currency]
    to_rate = rates[to_currency]
    result = amount / from_rate * to_rate

    save_history(
        user_id=message.from_user.id,
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency,
        result=result
    )

    await message.answer(
        f"💱 Результат конвертации\n\n"
        f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
    )

    await state.clear()

    await message.answer(
        "Выберите действие:",
        reply_markup=menu_keyboard
    )