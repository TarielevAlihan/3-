from aiogram import Router, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    kd = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [

                types.InlineKeyboardButton(text='Телефон', callback_data='+123456789'),
                types.InlineKeyboardButton(text='Адрес: улица, дом', callback_data='12:31:11'),
                types.InlineKeyboardButton(text='Наш инстаграм', url='https://www.instagram.com/'),
                types.InlineKeyboardButton(text='Отзывы от наших довольных клиентов', callback_data='GOOd,bad'),

            ]
        ]
    )
    await message.answer(f'Информация о нас,{message.from_user.first_name}', reply_markup=kd)

