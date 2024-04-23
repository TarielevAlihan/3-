from aiogram import types , F ,Router
from aiogram.filters import Command




keyboard_router = Router()
@keyboard_router.callback_query(F.data == 'info')
async def kb_cmd(callback: types.CallbackQuery):
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



        ]
    )
    await callback.message.answer(f'Информация о нас,{callback.from_user.first_name}', reply_markup=kd)

