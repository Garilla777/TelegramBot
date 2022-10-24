from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Привет, какие наши опции по печати интересуют?', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/unlimprintbot')

# @dp.message_handler(commands=['Режим_работы'])
async def unlimprint_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Работаем много и почти каждый день!\nЛучше всего позвонить или написать нам в соц.сети по этому вопросу и мы обязательно договоримся!\n+7-931-328-22-14 - рабочий тельчик\n+7-981-147-85-89 - Саша\n\nтелега|инста|вк @unlimprint')

# @dp.message_handler(commands=['Расположение_нашей_мастёры'])
async def unlimprint_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Unlimited Printing\nУральская, 17 корпус 6, 2 этаж (в коридоре сразу направо)\nhttps://go.2gis.com/pzpdzy\n\nНа карте 2gis указан вход в здание')

# @dp.message_handler(commands=['Меню'])
# async def unlimprint_menu_command(message : types.Message):
# 	for ret in cur.execute('SELECT * FROM menu').fetchall():
# 	   await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(unlimprint_open_command, commands=['Режим_работы'])
    dp.register_message_handler(unlimprint_place_command, commands=['Расположение_нашей_мастёры'])
	