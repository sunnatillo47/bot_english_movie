import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from utils.misc import subscription
from loader import bot

from keyboards.inline.subscription import check_button


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):        
        if update.message:
            user = update.message.from_user.id
            if update.message and update.message.text in ['/start', '/help']:
                return
        else:
            return

        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                result = f"Iltimos kanalga obuna bo'ling!"
        if not final_status:
            await update.message.answer(result,reply_markup=check_button, disable_web_page_preview=True)
            raise CancelHandler()