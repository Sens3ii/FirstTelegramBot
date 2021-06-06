from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callbacks import order_callback


def order_keys(item):
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Купить",
                                 callback_data=order_callback.new(id=item.get('id'), title=item.get('title'),
                                                                  price=item.get('price')
                                                                  )),
        ],
        [
            InlineKeyboardButton(text="👍", callback_data="like"),
            InlineKeyboardButton(text="👎", callback_data="dislike")
        ],
        [
            InlineKeyboardButton(text="Share",
                                 switch_inline_query=f'Нашел крутой товар тут, под названием {item.get("title")}')
        ]
    ])
    return keys
