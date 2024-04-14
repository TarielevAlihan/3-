import asyncio
from aiogram import Bot
import logging

from cofig import bot, dp
from handlers.start import start_router
from handlers.picture import pic_router
from handlers.info import info_router
from handlers.echo import echo_router
from handlers.menu import menu_router
async def main():

    # привязка роутеров
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(pic_router)
    dp.include_router(info_router)


    # в самом конце!
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())