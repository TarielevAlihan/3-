from aiogram import Router, types
from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()



@start_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Здраствуйте это бот "заведения вкусная еда" ')

    kd = types.InlineKeyboardMarkup(
        inline_keyboard=[

                [
                    types.InlineKeyboardButton(text='Картинка', callback_data='pic')
                ],

                [
                    types.InlineKeyboardButton(text='Рандомная картинка', callback_data='pic_random')
                ],

                [
                    types.InlineKeyboardButton(text='Информация о нас', callback_data='info')
                ],

                [
                    types.InlineKeyboardButton(text='Меню', callback_data='menu')
                ],

                [
                    types.InlineKeyboardButton(text="Пройти опрос", callback_data="survey")
                ],

        ]
    )
    await message.answer(f'Все вожмности бота,{message.from_user.first_name}', reply_markup=kd)












