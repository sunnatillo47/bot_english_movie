from aiogram import types
from data.config import CHANNELS, ADMINS
from keyboards.inline.subscription import check_button
from loader import bot, dp, db
from utils.misc import subscription

from keyboards.default.main_btn import main_btn, admin_btn

@dp.message_handler(commands=["start"], chat_id=ADMINS)
async def start_admin(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.full_name
    await message.answer("Admin xush kelibsiz!", reply_markup = admin_btn)
    try:
        db.add_user(id=user_id,
                    name=name)
    except:
            pass

    count = db.count_users()[0]
    msg = f"🛎 {message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=5879726928, text=msg)

@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.full_name
    for channel in CHANNELS:
        status = await subscription.check(user_id=message.from_user.id,
                                          channel=channel)
        
        if not status:
            await message.answer(f"<b>Quyidagi kanalga a'zo bo'ling va /start ni bosing\n\n/start /start /start</b>",
                         reply_markup=check_button,
                         disable_web_page_preview=True)
        if status:
            await message.answer("<b>👏 Muvoffiqiyatli!</b> marhamat botdan foydalaning!", reply_markup = main_btn)
            
            try:
                db.add_user(id=user_id,
                    name=name)
            except:
                pass

            count = db.count_users()[0]
            msg = f"🛎 <b><a href='https://t.me/{message.from_user.username}'>{message.from_user.full_name}</a></b> bazaga qo\'shildi.\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=5879726928, text=msg)
