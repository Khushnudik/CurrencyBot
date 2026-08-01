from aiogram import Router, F
from aiogram.types import Message

from services.history_service import get_history

router = Router()


@router.message(F.text == "📜 История")
async def history_handler(message: Message):
    history = get_history(message.from_user.id)

    if not history:
        await message.answer(
            "📜 История пуста.\n\n"
            "Сделайте первую конвертацию."
        )
        return

    text = "📜 История операций\n\n"

    for index, record in enumerate(history, start=1):
        date = record.created_at.strftime("%d.%m.%Y • %H:%M")

        text += (
            f"№{index}\n"
            f"📅 {date}\n"
            f"💱 {record.amount:.2f} {record.from_currency} → {record.to_currency}\n"
            f"✅ {record.result:.2f} {record.to_currency}\n\n"
        )

    text += f"📊 Всего операций: {len(history)}"

    await message.answer(text)
