from aiogram import Router, types
from aiogram.filters import Command
from aiogram import Router, types , F

start_router = Router()

@start_router.message(Command('start'))
async def start(command: types.Message):
    await command.answer('Good Morning!')


