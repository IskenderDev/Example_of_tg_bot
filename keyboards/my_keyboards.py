from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="like")],
        [KeyboardButton(text="dislike")],

    ]
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="About", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")],
        [InlineKeyboardButton(text="Our contacts 1 ", callback_data="contact1")],
        [InlineKeyboardButton(text="Our contacts 2 ", callback_data="contact2")],
    ]
)

