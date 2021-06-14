from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData("buy", "id", "title", "price", "photo_url")

order_callback = CallbackData("order", "id", "title", "price")
