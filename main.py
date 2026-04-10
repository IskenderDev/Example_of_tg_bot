import asyncio
from aiogram import Bot, Dispatcher
from handlers.comands import router as comands
from handlers.reply_ex import router as reply_ex
from handlers.inline_ex import router as inline_ex

TOKEN = '8380639746:AAHP9CiMmcjRGNRwVJ_kINBXLGRd_VGseYA'
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(comands)
dp.include_router(reply_ex)
dp.include_router(inline_ex)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Starting bot...')
    asyncio.run(main())