import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from src.db.models import database
from src.handlers import router

load_dotenv(".env")

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


async def on_startup(bot: Bot):
    await database.create_all()


async def on_shutdown(bot: Bot):
    pass
    # await database.drop_all()
    # await bot.delete_my_commands()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
