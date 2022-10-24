from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Меню')
b2 = KeyboardButton('/Расположение_нашей_мастёры')
b3 = KeyboardButton('/Режим_работы')
# b4 = KeyboardButton('Поделиться контактом', reguest_contact=True)
# b5 = KeyboardButton('Отправить геопозицию', reguest_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)#.row(b4, b5)

# row(b4,b5) добавление всех кнопок в строку
# insert(b3) расположение кнопки в пустом месте 