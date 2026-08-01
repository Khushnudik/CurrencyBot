from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

currency_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇸 USD"),
            KeyboardButton(text="🇪🇺 EUR")
        ],
        [
            KeyboardButton(text="🇷🇺 RUB"),
            KeyboardButton(text="🇹🇯 TJS")
        ]
    ],
    resize_keyboard=True
)