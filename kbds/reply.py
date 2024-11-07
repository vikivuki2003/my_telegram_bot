from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="About us"),
        ],
        {
            KeyboardButton(text="Payment options"),
            KeyboardButton(text="Delivery options"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder='What are you interested in?'
)

del_kbd = ReplyKeyboardRemove()


start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Menu"),
    KeyboardButton(text="About us"),
    KeyboardButton(text="Payment options"),
    KeyboardButton(text="Delivery options"),
)
start_kb2.adjust(2, 2)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text="Leave a review"),)


test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Create a poll", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Send phone number ☎️", request_contact=True),
            KeyboardButton(text="Senf location 🗺️", request_location=True),
        ],
    ],
    resize_keyboard=True,
)
