from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from states import Form


@dp.message_handler(Command("form"))
async def enter_form(message: types.Message):
    await message.answer("Заполните данные по порядку.\n"
                         "Введите ваше имя:")
    await Form.first()


@dp.message_handler(state=Form.Q1)
async def answer_name(message: types.Message, state: FSMContext):
    name_ = message.text
    await state.update_data(name=name_)

    await message.answer("Введите ваш email:")
    await Form.next()


@dp.message_handler(state=Form.Q2)
async def answer_email(message: types.Message, state: FSMContext):
    email_ = message.text
    await state.update_data(email=email_)

    await message.answer("Введите ваш номер телефона:")
    await Form.next()


@dp.message_handler(state=Form.Q3)
async def answer_number(message: types.Message, state: FSMContext):
    form_data = await state.get_data()
    name_ = form_data.get("name")
    email_ = form_data.get("email")
    number_ = message.text

    await message.answer("Привет. FSM сохранила следующие данные:\n"
                         f"Имя: {name_}\n"
                         f"Email: {email_}\n"
                         f"Телефон: {number_}\n")
    await state.reset_state()
