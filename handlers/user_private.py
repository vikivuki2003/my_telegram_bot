from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, I'm a virtual assistant")


@user_private_router.message(Command('menu', 'name'))
async def menu_cmd(message: types.Message):
    await message.answer("Our menu:")