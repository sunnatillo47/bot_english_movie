
import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from utils.misc import subscription
from loader import bot


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):        
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        else:
            return

        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)

        if not final_status:
            raise CancelHandler()