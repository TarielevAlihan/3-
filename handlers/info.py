
from aiogram import Router, types , F

info_router = Router()
@info_router.callback_query(F.data == 'contact')
async def send_contact(callback: types.CallbackQuery):
    await callback.message.answer("Телефон: +123456789\nEmail: example@example.com")

@info_router.callback_query(F.data == 'info_institution')
async def send_about_us(callback: types.CallbackQuery):
    await callback.message.answer("Мы - ваше любимое заведение! Отличная кухня, уютная атмосфера и отзывчивый персонал.")


@info_router.callback_query(F.data == 'review')
async def send_reviews(callback: types.CallbackQuery):
    await callback.message.answer("Отзывы от наших довольных клиентов:\n1. Очень вкусно!\n2. Приятное обслуживание.")

@info_router.callback_query(F.data == 'address')
async def address(callback: types.CallbackQuery):
    await callback.message.answer("Улица пушкина 112 Здание 25")
