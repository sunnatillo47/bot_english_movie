from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

etn_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👍", callback_data="like"),
            InlineKeyboardButton(text="👎", callback_data="dislike")
        ]
    ]
)

send_bot = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Ulashish ↗️", switch_inline_query="**Ingliz tildagi filmlar bazasi +subtitel 👇👇👇**\n\n**🤖 @EngMovieBase_Bot**")
        ]
    ]
)
