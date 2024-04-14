from aiogram import types , F ,Router
from aiogram.filters import Command




keyboard_router = Router()
@keyboard_router.message(Command('info'))
async def KB_cmd(message: types.Message):
    kd = types.InlineKeyboardMarkup(
        inline_keyboard=[

                [
                    types.InlineKeyboardButton(text='Телефон', callback_data='contact')
                ],

                [
                    types.InlineKeyboardButton(text='О заведеинии', callback_data='info_institution')
                ],

                [
                    types.InlineKeyboardButton(text='Адрес:', callback_data='address')
                ],

                [
                    types.InlineKeyboardButton(text='Наш инстаграм', url='https://www.instagram.com/')
                ],

                [
                    types.InlineKeyboardButton(text='Отзывы от наших довольных клиентов', callback_data='review')
                ],

                [
                    types.InlineKeyboardButton(text="Пройти опрос", callback_data="survey")
                ],


        ]
    )
    await message.answer(f'Информация о нас,{message.from_user.first_name}', reply_markup=kd)

