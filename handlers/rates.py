from aiogram import Router, F
from aiogram.types import Message

from services.currency_service import get_rates

router = Router()


@router.message(F.text == "📈 Курсы валют")
async def rates_handler(message: Message):
    try:
        data = get_rates()
        rates = data["rates"]
        update_time = data["update_time"]

        usd = rates["USD"]
        eur = rates["EUR"]
        rub = rates["RUB"]
        tjs = rates["TJS"]

        usd_to_tjs = tjs
        eur_to_tjs = tjs / eur
        rub_to_tjs = tjs / rub

        await message.answer(
            f"📈 Актуальные курсы валют\n\n"
            f"🇺🇸 1 USD = {usd_to_tjs:.2f} TJS\n\n"
            f"🇪🇺 1 EUR = {eur_to_tjs:.2f} TJS\n\n"
            f"🇷🇺 1 RUB = {rub_to_tjs:.4f} TJS\n\n"
            f"🕒 Обновлено:\n"
            f"{update_time}"
        )

    except Exception:
        await message.answer(
            "❌ Не удалось получить актуальные курсы.\n\n"
            "🌐 Проверьте подключение к интернету и попробуйте снова."
        )