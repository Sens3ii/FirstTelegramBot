from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline import edit
from loader import dp


@dp.message_handler(Command("edit"))
async def show_items(message: Message):
    await message.answer(text=
                         "Edit @2BForMe info.\n"
                         "Name: Test Bot\n"
                         "Description: Abrakadabra\n"
                         "About: About?\n"
                         "Botpic: 2B\n"
                         "Commands: /edit\n",
                         reply_markup=edit.keyboard
                         )


@dp.callback_query_handler(text="cancel")
async def cancel_bot(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
