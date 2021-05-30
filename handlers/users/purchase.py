import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.items_buttons import choice, coffee_keyboard
from loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text="Привет друг. У нас есть 2 товара мы бомжи, но дальше больше.\n"
                              "Выбирай на свой вкус дружище.",
                         reply_markup=choice
                         )


@dp.callback_query_handler(buy_callback.filter(item_name="coffee"))
async def buying_coffee(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get("quantity")
    await call.message.answer(f'Вы выбрали кофе. Кол-во: {quantity}',
                              reply_markup=coffee_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="tea"))
async def buying_tea(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get("quantity")
    await call.message.answer(f'Вы выбрали чай. Кол-во: {quantity}')


@dp.callback_query_handler(text='cancel')
async def buying_tea(call: CallbackQuery):
    await call.answer('Отмена...', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
