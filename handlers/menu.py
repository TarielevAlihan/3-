from aiogram.filters import Command
from aiogram import Router, types , F




menu_router = Router()


@menu_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    kd = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Блюда'),
                types.KeyboardButton(text='Напитки'),
                types.KeyboardButton(text='Десерты')
            ]
        ]
    )
    await message.answer("Выберите категорию меню:", reply_markup=kd)


@menu_router.message(F.text == 'Блюда')
async def menu_disnes(message: types.Message):
    await message.answer(f"овощной суп \n"
                         f"жаркое из говядины \n"
                         f"роллы")

@menu_router.message(F.text == 'Напитки')
async def menu_drinks(message: types.Message):
    await message.answer(f"лимонад \n"
                         f"кокакола\n"
                         f"спрайт")


@menu_router.message(F.text == 'Десерты')
async def menu_drink(message: types.Message):
    await message.answer(f"чискейк \n"
                         f"крем_брюле\n"
                         f"мороженое")


