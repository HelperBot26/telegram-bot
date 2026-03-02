import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🚀 Открыть материал",
                url="https://твойсайт.ru"
            )]
        ]
    )

    text = (
        "🔥 <b>Добро пожаловать!</b>\n\n"
        "Здесь будет ваше описание.\n\n"
        "Нажмите кнопку ниже 👇"
    )

    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
