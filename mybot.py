import telebot
import pygsheets
import time
TOKEN = '5719851205:AAF-g4aYF6_IfZyDLYO3RcLbPxyXRJxIlKM'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['AgIAAxkBAAEBf95jjHTrpS-9g4ZnKak8IW5JRj0kdQACHgADZ8j4Ipl0YqyHEWzpKwQ', ])
def start_message(message):
    while True:
        try:
            chat_id = message.chat.id
            gc = pygsheets.authorize(service_file='creds.json')
            sh = gc.open_by_url(
                'https://docs.google.com/spreadsheets/d/1SmBSeig_GSEftIT6Zpqx8dhWP4Bf7CjVnb0VJw48feY/edit#gid=367067341')
            sheet = sh.sheet1
            bot.send_message(chat_id, f'Добуштардын саны/Количество голосов: {sheet.rows} \n'
                                      f'ЗаЯпошки үчүн добуштарды билүү үчүн, ушул шилтемеге кириңиз https://zayaposhki.stars.kg/')

            time.sleep(1800)
        except:
            pass


if __name__ == '__main__':
    bot.polling()
