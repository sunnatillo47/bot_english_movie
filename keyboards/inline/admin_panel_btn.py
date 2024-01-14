from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

panel_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="➕ Add movie", callback_data="add_movie"),
            InlineKeyboardButton(text="🗑 Delete movie", callback_data="del_movie")
        ],
        # [
        #     InlineKeyboardButton(text="🔝 Top up", callback_data="top_up")
        # ],
        [
            InlineKeyboardButton(text="📊 BotStat", callback_data="stat")
        ],
        [
            InlineKeyboardButton(text = "📩 Send a message", callback_data="send_msg")
        ]
    ]
)