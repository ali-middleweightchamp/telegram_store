from aiogram import Bot, Dispatcher   
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.config import config


bot = Bot(
    token=config,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer("Добро пожаловать в Electronics bot")

