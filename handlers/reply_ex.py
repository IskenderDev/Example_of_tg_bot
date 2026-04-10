from keyboards.my_keyboards import keyboard
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
likes = 0
dislikes = 0


@router.message(Command("reply"))
async def reply(message: Message):
    await message.answer("Вот ваши кнопки", reply_markup=keyboard)


@router.message(F.text == 'like')
async def like(message: Message):
    global likes
    likes += 1
    await message.answer(f"Likes {likes}")


@router.message(F.text == 'dislike')
async def dislike(message: Message):
    global dislikes
    dislikes += 1
    await message.answer(f"Dislikes {dislikes}")
