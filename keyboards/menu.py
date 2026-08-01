from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💱 Конвертация валют")],
        [KeyboardButton(text="📈 Курсы валют")],
        [KeyboardButton(text="📜 История")],
        [KeyboardButton(text="ℹ️ Помощь")]
    ],
    resize_keyboard=True
)