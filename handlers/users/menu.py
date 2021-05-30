from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer("Выберите товар из меню ниже", reply_markup=menu)


@dp.message_handler(text="Кофе")
async def get_coffee(message: types.Message):
    await message.answer("Вы выбрали Кофе")


@dp.message_handler(Text(equals=['Сахар', 'Молоко']))
async def get_syrup(message: types.Message):
    await message.answer(f'Вы выбрали одну из добавок: {message.text}', reply_markup=ReplyKeyboardRemove())
