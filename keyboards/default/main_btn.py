
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_btn = ReplyKeyboardMarkup(
        keyboard = [
                [
                        KeyboardButton(text="🔍 Kino qidirish")
                ],
                [         
                        KeyboardButton(text="🏆 Top kinolar")
                ],
        ],
        resize_keyboard=True
)

admin_btn = ReplyKeyboardMarkup(
        keyboard = [
                [
                        KeyboardButton(text="🔍 Kino qidirish")
                ],
                [
                        KeyboardButton(text="🏆 Top kinolar")
                ],
                [
                    KeyboardButton(text="🎛 Admin panel")
                ]
        ],
        resize_keyboard=True
)

back_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ]
)