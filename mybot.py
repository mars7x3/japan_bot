import telebot
import pygsheets
from telebot import types

gc = pygsheets.authorize(service_file='creds.json')

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1SmBSeig_GSEftIT6Zpqx8dhWP4Bf7CjVnb0VJw48feY/edit#gid=367067341')
sheet = sh.sheet1

TOKEN = '5719851205:AAF-g4aYF6_IfZyDLYO3RcLbPxyXRJxIlKM'
bot = telebot.TeleBot(TOKEN)

btn1 = types.InlineKeyboardButton('Количество заявок')
inline_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
inline_keyboard.add(btn1)


@bot.message_handler(commands=['start', ])
def start_message(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, f'Вас приветствует бот!', reply_markup=inline_keyboard)
    bot.register_next_step_handler(msg, inline)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    chat_id = c.chat.id
    msg = bot.send_message(chat_id, f'{sheet.rows}')
    bot.register_next_step_handler(msg, inline)


bot.polling()