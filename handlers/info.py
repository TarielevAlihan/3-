from aiogram.filters import Command
from aiogram import Router, types


info_router = Router()

@info_router.message(Command('info'))
async def send_address(message):

    address = "Адрес: улица, дом"
    message.reply(address)



@info_router.message(Command('contact'))
async def send_contact(message):
    contacts = "Телефон: +123456789\nEmail: example@example.com"
    message.reply(contacts)

@info_router.message(Command('info_institution'))
async def send_about_us(message):
    about_us = "Мы - ваше любимое заведение! Отличная кухня, уютная атмосфера и отзывчивый персонал."
    message.reply(about_us)

@info_router.message(Command('review'))
async def send_reviews(message):
    reviews = "Отзывы от наших довольных клиентов:\n1. Очень вкусно!\n2. Приятное обслуживание."
    message.reply(reviews)