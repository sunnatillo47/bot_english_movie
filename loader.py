from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database
from utils.db_api.movie_base import MovieDB
from utils.db_api.user_voites import Voitesbase
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db = "data/main.db")
mov_db = MovieDB(path_to_db = "data/movie.db")
voites_db = Voitesbase(path_to_db = "data/voites.db")