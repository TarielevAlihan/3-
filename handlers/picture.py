from aiogram.filters import Command
from aiogram.types import FSInputFile
import os
from aiogram import Router, F, types
from random import choice

pic_router = Router()


@pic_router.callback_query(F.data == 'pic')
async def pic(callback: types.CallbackQuery):
    path = 'images/images.jpeg'
    file = FSInputFile(path)
    await callback.message.answer_photo(photo=file, caption='красивая фотка')

@pic_router.callback_query(F.data == 'pic_random')
async def pic_random(callback: types.CallbackQuery):
    photos = os.listdir('images/')
    path = f'images/{choice(photos)}'
    file = FSInputFile(path)
    await callback.message.answer_photo(photo=file, caption='красивая фотка')