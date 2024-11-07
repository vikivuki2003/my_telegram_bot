from aiogram import F, Router, types
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds.reply import get_keyboard


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


ADMIN_KB = get_keyboard(
    "Add product",
    "Change product",
    "Delete product",
    "Just to look at it",
    placeholder="Choose action",
    sizes=(2, 1, 1),
)


@admin_router.message(Command("admin"))
async def add_product(message: types.Message):
    await message.answer("What do you want to do?", reply_markup=ADMIN_KB)


@admin_router.message(F.text == "Just to look at it")
async def starring_at_product(message: types.Message):
    await message.answer("OK, There is a list of products")


@admin_router.message(F.text == "Change product")
async def change_product(message: types.Message):
    await message.answer("OK, There is a list of products")


@admin_router.message(F.text == "Delete product")
async def delete_product(message: types.Message):
    await message.answer("Select the item(s) to delete")


@admin_router.message(F.text == "Add product")
async def add_product(message: types.Message):
    await message.answer(
        "Enter the product name", reply_markup=types.ReplyKeyboardRemove()
    )


@admin_router.message(Command("cancel"))
@admin_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: types.Message) -> None:
    await message.answer("Actions canceled", reply_markup=ADMIN_KB)


@admin_router.message(Command("back"))
@admin_router.message(F.text.casefold() == "back")
async def cancel_handler(message: types.Message) -> None:
    await message.answer(f"OK, you're back to the last step.")


@admin_router.message(F.text)
async def add_name(message: types.Message):
    await message.answer("Enter the product description")


@admin_router.message(F.text)
async def add_description(message: types.Message):
    await message.answer("Enter the price of the product")


@admin_router.message(F.text)
async def add_price(message: types.Message):
    await message.answer("Upload an image of the product")


@admin_router.message(F.photo)
async def add_image(message: types.Message):
    await message.answer("The product added", reply_markup=ADMIN_KB)