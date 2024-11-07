from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils.formatting import Text

from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, I'm a virtual assistant")


# @user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(Text(equals="menu", ignore_case=True))
async def menu_cmd(message: types.Message):
    await message.answer("Our menu:")


@user_private_router.message(F.text.lower() == "About us")
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("About us:")


@user_private_router.message(F.text.lower() == "Payment options")
@user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    await message.answer("Our payment options:")


@user_private_router.message((F.text.lower().contains('delivery')) | (F.text.lower() == 'Delivery options'))
@user_private_router.message(Command("shipping"))
async def menu_cmd(message: types.Message):
    await message.answer("Delivery options:")