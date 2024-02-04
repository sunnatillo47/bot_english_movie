from aiogram import types
from loader import dp,mov_db, voites_db
from aiogram.dispatcher import FSMContext
from data.config import ADMINS

import re
from keyboards.inline.admin_panel_btn import panel_menu
from keyboards.inline.evaluation import etn_btn, send_bot

@dp.message_handler(text="🔍 Kino qidirish")
async def movie_search(message: types.Message, state: FSMContext):
    await message.answer("<b>Kino kodini yuboring 🔍</b>")
    await state.set_state("search")

@dp.message_handler(state = "search")
async def get_id(message: types.Message, state: FSMContext):
    mov_get_id = message.text
    user_id = message.from_user.id
    users_id = voites_db.select_all_voites(movie_id_ref=mov_get_id)

    son = ""
    numbers = []
    for n in users_id:
        for i in str(n):
            if i.isdigit():
                son += i
        if son:
            numbers.append(int(son))
        son = ""
    try:
            if user_id in numbers:
                movie_format = mov_db.get_movie_info(id=mov_get_id)[1]
                movie_caption = f"<b>{mov_db.get_movie_info(id=mov_get_id)[2]}</b>"
                movie_caption += f"\n\n<b>🤖 @EngMovieBase_Bot</b>"
                await message.answer_document(movie_format, caption = movie_caption, reply_markup=send_bot)
            else:
                movie_format = mov_db.get_movie_info(id=mov_get_id)[1]
                movie_caption = f"<b>{mov_db.get_movie_info(id=mov_get_id)[2]}</b>"
                movie_caption += f"\n\n<b>🤖 @EngMovieBase_Bot</b>"
                await message.answer_document(movie_format, caption = movie_caption, reply_markup=etn_btn)

    except:
        await message.answer("<b>⚠️ Siz yuborgan kodda kino topilmadi!</b>")


    await state.finish()

# voites to movie
    
@dp.callback_query_handler(text=["like", "dislike"])
async def process_etn_callback(query: types.CallbackQuery):
    # num = int(query.message.caption.split("\n")[0])
    movie_id = int(re.search(r'\d+', query.message.caption).group())
    # await message.answer(num)
    user_id = query.from_user.id
    callback_data = query.data

    if callback_data == "like":
        
        like_plus = mov_db.get_movie_info(movie_id)[3] + 1
        mov_db.update_like(like=like_plus, id=movie_id)
        voites_db.add_voites(movie_id_ref=movie_id, user_id=user_id)
        await query.answer("👍 +1")    

    elif callback_data == "dislike":

        dislike_plus = mov_db.get_movie_info(movie_id)[4] + 1
        mov_db.update_like(like=dislike_plus, id=movie_id)
        voites_db.add_voites(movie_id_ref=movie_id, user_id=user_id)
        await query.answer("👎 +1")

    await query.message.edit_reply_markup(send_bot)
    

@dp.message_handler(text="🏆 Top kinolar")
async def top_movie(message: types.Message):
    try: 
        msg = ""
        for n in range(len(mov_db.top_movies())):
            top_mov = mov_db.top_movies()[n]
            text = mov_db.top_movies()[n][0]
            lines = text.split('\n') # kinoning nomini oladi
            get_id = int(re.search(r'\d+', lines[0]).group()) # kino idsini oladi
            msg += f"{n+1}. <b>{lines[1]}</b>\n<i>{lines[2]}</i> \n<code>Kod: {get_id} | {top_mov[1]}👍</code>\n\n"
        msg += f"\n\n<b>🤖 @EngMovieBase_Bot</b>"
        await message.answer(msg)
    except:
        await message.answer("<b>Top filmlar yangilanishini kuting</b>")
@dp.message_handler(text="🎛 Admin panel", chat_id = ADMINS)
async def admin_panel(message: types.Message):
    await message.answer("<b>Admin paneliga xush kelibsiz</b>", reply_markup = panel_menu)