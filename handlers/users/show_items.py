import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callbacks import buy_callback, order_callback
from keyboards.inline.items import choice
from keyboards.inline.order import order_keys
from loader import dp, bot


@dp.message_handler(Command('show_items'))
async def show_items(message: Message):
    await message.answer(text="Выберите нужный товар \n",
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter())
async def show_item(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.bot.send_photo(chat_id=call.message.chat.id, photo=callback_data.get('photo_url'),
                              caption=callback_data.get('title'), reply_markup=order_keys(callback_data))


@dp.callback_query_handler(order_callback.filter())
async def order_item(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    await call.message.edit_caption(f'Вы купили {callback_data.get("title")}!', reply_markup=None)


@dp.callback_query_handler(text_contains="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text='Вы отменили действие',
                                 reply_markup=None)


# @dp.callback_query_handler(text_contains="share")
# async def cancel_buying(call: CallbackQuery):
#     await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="dislike")
async def give_dislike(call: CallbackQuery):
    await call.answer("Вы поставили dislike", show_alert=True, cache_time=60)


@dp.callback_query_handler(text_contains="like")
async def give_like(call: CallbackQuery):
    await call.answer("Вы поставили like", show_alert=True, cache_time=60)
