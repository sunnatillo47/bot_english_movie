from loader import dp,mov_db
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

@dp.callback_query_handler(text="add_movie")
async def add_movie(call: CallbackQuery, state: FSMContext):
        await call.message.answer("<b>Kino yuboring</b>")
        await state.set_state("movie_get_id")

@dp.message_handler(state="movie_get_id", content_types = types.ContentType.VIDEO)
@dp.message_handler(state="movie_get_id", content_types = types.ContentType.DOCUMENT)
async def get_id(message: types.Message, state: FSMContext):
        # bu yerda types.ContentType.DOCUMENT faqat shuni o'zini qo'llasa bo'larkan, ishni ko'paytirimman
        if message.content_type == types.ContentType.VIDEO:
            different = "VIDEO"
            id = message.video.file_id
            await state.update_data(movie_id=id)
            await state.update_data(diff = different)

        elif message.content_type == types.ContentType.DOCUMENT:
            different = "DOCUMENT"
            id = message.document.file_id
            await state.update_data(movie_id=id)
            await state.update_data(diff = different)

        await message.answer("<b>Kinoga sarlavha kiritig</b>\n\n<i>Faqat kinoga beriladigan kod\nKinoga tavsif</i>")
        await state.set_state("mov_caption")

@dp.message_handler(state="mov_caption")
async def movie_get_caption(message: types.Message, state: FSMContext):
    mov_caption = message.text
    await state.update_data(mov_cap = mov_caption)
    
    await message.answer("Yuqoridagi kinoga berilgan kodni tasdiqlang☝️.")
    await state.set_state("mov_id")

@dp.message_handler(state = "mov_id")
async def mov_id(message: types.Message, state: FSMContext):
    try:
        mov_id = message.text
        data = await state.get_data()
        movie_id = data.get("movie_id")
        mov_caption = data.get("mov_cap")
        diff = data.get("diff")

        mov_db.add_movie(id = mov_id, movie_id=movie_id, movie_caption=mov_caption, like=0, dislike=0)
    except:
         await message.answer("<b>Menimcha bu idli kino bor\nBoshidan boshlang!</b>")
         await state.finish()
    
    mdb = mov_db.get_movie_info(id=mov_id)
    try:
        if diff == "VIDEO":
            await message.answer_video(mdb[1], caption=mdb[2])
        elif diff == "DOCUMENT":
            await message.answer_document(mdb[1], caption=mdb[2])
    except:
         await message.answer("Xatolik yuzaga keldi")

    await state.finish()



@dp.callback_query_handler(text="del_movie")
async def del_movie(call: CallbackQuery, state: FSMContext):
        await call.message.answer("<b>O'chirmoqchi bo'lgan kino idsini yuboring!</b>")
        await state.set_state("movie_del")

@dp.message_handler(state = "movie_del")
async def del_movie(message: types.Message, state: FSMContext):
     try:
        id = message.text
        mov_db.del_movie(id=id)
        await message.answer("O'chirildi")
        await state.finish()
     except:
          await message.answer("<b>O'chirib bo'lmadi yoki bunday idli kino botda yo'q</b>")
          await state.finish()
