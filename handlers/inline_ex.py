from keyboards.my_keyboards import inline_keyboard
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

router = Router()

@router.message(Command("inline"))
async def reply(message: Message):
    await message.answer("Вот ваши кнопки", reply_markup=inline_keyboard)

@router.callback_query(F.data == 'contact')
async def contact(callback: CallbackQuery):
    await callback.message.answer("А не дам тееб нормер ")


