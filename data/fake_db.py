from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    price: int
    photo_link: str


coffee_1 = Item(0, 'Американо', 20,
                'imgur.com/JDI6wWw')
coffee_2 = Item(1, 'Латте', 30,
                'i.imgur.com/cPNQEqY.jpg')
coffee_3 = Item(2, 'Капучино', 32,
                'i.imgur.com/yWmqhXo.jpg')
coffee_4 = Item(3, 'Экспрессо', 26,
                'i.imgur.com/RPDTgRp.jpeg')
coffee_5 = Item(4, 'Мокка', 22,
                'i.imgur.com/yWmqhXo.jpg')

items = [coffee_1, coffee_2, coffee_3, coffee_4, coffee_5]
print(items)
