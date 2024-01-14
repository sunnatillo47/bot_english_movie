from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="KINO TV 📽️", url = "https://t.me/kino_englishmovie" ,callback_data="channel_1")
        ]
    ]
)