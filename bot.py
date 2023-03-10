import telebot
import random
import time
from telebot import types
from config import TOKEN

# skip_pending включает ответ только на последнее сообщение при перезапуске
bot=telebot.TeleBot(token = TOKEN, skip_pending=True)   


sms = open('itog.txt','r', encoding='utf-8') # считываем файл с сообщениями
lineslist = sms.readlines() # разбиваем по строкам


markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
markup.add(itembtn1)

#start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, я Равлик. Напиши /help')

#help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/show")
    btn2 = types.KeyboardButton("/lick")
    btn3 = types.KeyboardButton("/say")
    markup.add(btn1, btn2, btn3)
    bot.reply_to(message, 'Равлик бот V1.3. Доступные команды: /show, /lick, /say ', reply_markup=markup)
    
last_time = {}
#основа
@bot.message_handler(content_types=['text'])
def send_text(message):
    # защита от спама
    if message.chat.id not in last_time:
        last_time[message.chat.id] = time.time()
        # основная часть
        if message.text=="/show":
            photo = open('2323.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text=="/lick":
            doc = open('monkey.gif', 'rb')
            bot.send_animation(message.chat.id, doc)

        elif message.text=="/say":
            rm = random.randint(0,len(lineslist)-1)
            bot.send_message(message.chat.id, lineslist[rm])
    else:
        if (time.time() - last_time[message.chat.id]) * 1000 < 500: # 500мс ограничение на дудос
            bot.send_message(message.chat.id,'Нах ты дудосишь')
            return 0

        last_time[message.chat.id] = time.time()
        # основная часть
        if message.text=="/show":
            photo = open('2323.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)

        elif message.text=="/lick":
            doc = open('monkey.gif', 'rb')
            bot.send_animation(message.chat.id, doc)

        elif message.text=="/say":
            rm = random.randint(0,len(lineslist))
            bot.send_message(message.chat.id, lineslist[rm])





bot.polling()