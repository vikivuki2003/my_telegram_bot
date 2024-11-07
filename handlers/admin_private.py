from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

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

class AddProduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    image = State()

    texts = {
        'AddProduct:name': 'Re-enter the name:',
        'AddProduct:description': 'Re-enter the description:',
        'AddProduct:price': 'Re-enter the price:',
        'AddProduct:image': 'This state is the last one, therefore...',
    }


@admin_router.message(StateFilter(None), F.text == "Add product")
async def add_product(message: types.Message, state: FSMContext):
    await message.answer(
        "Enter the product name", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(AddProduct.name)

@admin_router.message(StateFilter('*'), Command("cancel"))
@admin_router.message(StateFilter('*'), F.text.casefold() == "cancel")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Actions canceled", reply_markup=ADMIN_KB)

@admin_router.message(StateFilter('*'), Command("back"))
@admin_router.message(StateFilter('*'), F.text.casefold() == "back")
async def back_step_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()

    if current_state == AddProduct.name:
        await message.answer('There is no previous step, either enter the product name or write "cancel"')
        return

    previous = None
    for step in AddProduct.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f"OK, you're back to the last step. \n {AddProduct.texts[previous.state]}")
            return
        previous = step


@admin_router.message(AddProduct.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
    if len(message.text) >= 100:
        await message.answer("The product name must not exceed 100 characters. \n Enter again")
        return

    await state.update_data(name=message.text)
    await message.answer("Enter the product description")
    await state.set_state(AddProduct.description)

@admin_router.message(AddProduct.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("You have entered invalid data, enter the text of the product name")

@admin_router.message(AddProduct.description, F.text)
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Enter the price of the product")
    await state.set_state(AddProduct.price)


@admin_router.message(AddProduct.price, F.text)
async def add_price(message: types.Message, state: FSMContext):
    try:
        float(message.text)
    except ValueError:
        await message.answer("Enter the correct price value")
        return

    await state.update_data(price=message.text)
    await message.answer("Upload an image of the product")
    await state.set_state(AddProduct.image)

@admin_router.message(AddProduct.price)
async def add_price2(message: types.Message, state: FSMContext):
    await message.answer("You have entered invalid data, enter the cost of the product")

@admin_router.message(AddProduct.image, F.photo)
async def add_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    await message.answer("The product added", reply_markup=ADMIN_KB)
    data = await state.get_data()
    await message.answer(str(data))
    await state.clear()

@admin_router.message(AddProduct.image)
async def add_image2(message: types.Message, state: FSMContext):
    await message.answer("Send a photo of the food")

