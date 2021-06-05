from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Edit name", callback_data="edit:name"),
        InlineKeyboardButton(text="Edit description", callback_data="edit:description")
    ],
    [
        InlineKeyboardButton(text="Edit about", callback_data="edit:about"),
        InlineKeyboardButton(text="Edit botpic", callback_data="edit:botpic")
    ],
    [
        InlineKeyboardButton(text="Edit commands", callback_data="edit:commands"),
        InlineKeyboardButton(text="Cancel", callback_data="cancel")
    ],
])
