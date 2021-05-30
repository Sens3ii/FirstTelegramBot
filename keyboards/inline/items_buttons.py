from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Купить кофе',
            callback_data=buy_callback.new(item_name='coffee', quantity=1)
        ),
        InlineKeyboardButton(
            text='Купить чай',
            callback_data="buy:tea:2"
        )
    ],
    [
        InlineKeyboardButton(
            text='Отмена',
            callback_data='cancel'
        )
    ]
])

coffee_keyboard = InlineKeyboardMarkup()

COFFEE_LINK = 'https://www.starbucks.com.kz/menu/drinks/espresso-based-drinks/caffee-latte'
coffee_link = InlineKeyboardMarkup(text="Купи тут", url=COFFEE_LINK)
coffee_keyboard.insert(coffee_link)
