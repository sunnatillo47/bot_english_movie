from loader import db,dp,mov_db
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

@dp.callback_query_handler(text="stat")
async def stat(call: CallbackQuery):
        msg = f"📊 Bot statistikasi\n\n"
        msg += f"👥 Foydalanuvchilar soni: {db.count_users()[0]}\n"
        msg += f"🗄 Botda kinolar soni: {mov_db.count_movies()[0]}"
        await call.message.answer(msg)

# @dp.callback_query_handler(text="top_up")
# async def stat(call: CallbackQuery, state: FSMContext):
        
#         await call.message.answer("Topga chiqarmoqchi bo'lgan kino idsini yuboring")
#         await state.set_state("top_id")

# @dp.message_handler(state="top_id")
# async def top_up(message: types.Message, state: FSMContext):
#         movie_id = message.text
#         await state.update_data(movie_id=movie_id)
#         await message.answer("👍 - nechtaga o'zgartirilsin")
#         await state.set_state("top")

# @dp.message_handler(state="top")
# async def top_upp(message: types.Message, state: FSMContext):
#     like_count = message.text
#     data = await state.get_data()
#     mov_id = data.get("movie_id")
#     mov_db.update_top(like=like_count, id=mov_id)
#     await message.answer("Holat: muaffaqiyatli")
#     await state.finish()
        