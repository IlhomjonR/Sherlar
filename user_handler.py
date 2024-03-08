from loader import dp
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from database import add_sher
import random


@dp.message_handler(commands=['start'])
async def start_commad(message: types.Message):
    await message.answer("Salom")


@dp.message_handler(commands=['sher'])
async def start_sher(message: types.Message):
    random_sher = await add_sher()
    random_sher2 = random.choice(random_sher)[1]
    await message.answer(random_sher2)
