from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.menu import menu_keyboard

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "👋 Добро пожаловать в CurrencyBot!\n\n"
        "Выберите действие:",
        reply_markup=menu_keyboard
    )