from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
import asyncio


@dp.callback_query_handler(text="send_msg")
async def get_count(call: types.CallbackQuery, state: FSMContext):
        await call.message.answer('<b>Xabar yuboring!📝</b>')
        await state.set_state("rek")

@dp.message_handler(content_types=ContentType.ANY, state="rek")
async def get_test(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        for user in users:
            user_id = user[0]
            await message.send_copy(chat_id=user_id)
            await asyncio.sleep(0.05)
    except:
        print('Xatolik yuz berdi')
    await state.finish()