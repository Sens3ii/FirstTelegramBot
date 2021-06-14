from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.fake_db import items
from keyboards.inline.callbacks import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

for item in items:
    print(item.id, item.title, item.price)
    btn = InlineKeyboardButton(text=item.title,
                               callback_data=buy_callback.new(id=item.id, title=item.title, price=item.price,
                                                              photo_url=item.photo_link))
    choice.insert(btn)

cancel_btn = InlineKeyboardButton(text="Отмена", callback_data='cancel')
choice.insert(cancel_btn)
