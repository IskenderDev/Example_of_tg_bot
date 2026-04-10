import aiohttp
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


# --- Как получать даные через API ---

async def get_data_api(url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data
    except Exception as e:
        print(f"Что то упало я не знаю что вот ошиюка{e}")

# ------------------------------------

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Бот запус иницализация я не знаю что еще сказать ну напиши /help")


@router.message(Command("help"))
async def help(message: Message):
    await message.answer("/reply - появляется кнопки \n /inline - появляется кнопки только внизу текста   ")

@router.message(Command("api"))
async def api(message: Message):
    data = await get_data_api("https://jsonplaceholder.typicode.com/posts/1")
    await message.answer(data.get("title"))