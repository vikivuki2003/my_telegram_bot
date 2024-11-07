from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold #Italic, as_numbered_list и тд

from filters.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, I'm a virtual assistant",
                         reply_markup=reply.start_kb3.as_markup(
                            resize_keyboard=True,
                            input_field_placeholder='What are you interested in?'))


@user_private_router.message(F.text.lower() == "menu")
async def menu_cmd(message: types.Message):
    await message.answer("Our menu:")


@user_private_router.message(F.text.lower() == "About us")
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("About our shop:")


@user_private_router.message(F.text.lower() == "payment options")
@user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):

    text = as_marked_section(
            Bold("Payment options:"),
            "With a card in bot",
            "Upon receipt by card/cache",
            "In a cafe",
            marker='✅ '
        )
    await message.answer(text.as_html())


@user_private_router.message(
    (F.text.lower().contains("delivery")) | (F.text.lower() == "Delivery options")
)
@user_private_router.message(Command("shipping"))
async def menu_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Delivery options:"),
            "Courier",
            "Takeaway",
            "Dine in",
            marker='✅ '
        ),
        as_marked_section(
            Bold("Forbidden:"),
            "Mail",
            "Pigeons",
            marker='❌ '
        ),
        sep='\n----------------------\n'
    )
    await message.answer(text.as_html())


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"The phone number has been received")
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"The location has been received")
    await message.answer(str(message.location))