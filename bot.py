import telebot
from MyToken import token
from telebot import types
from  parsing import main
from parsing import title_
from parsing import big_title
from parsing import list_img

bot = telebot.TeleBot(token)

entry = {}

    

inline_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton("1", callback_data="1")
btn2 = types.InlineKeyboardButton("2", callback_data="2")
btn3 = types.InlineKeyboardButton("3", callback_data="3")
btn4 = types.InlineKeyboardButton("4", callback_data="4")
btn5 = types.InlineKeyboardButton("5", callback_data="5")
btn6 = types.InlineKeyboardButton("6", callback_data="6")
btn7 = types.InlineKeyboardButton("7", callback_data="7")
btn8 = types.InlineKeyboardButton("8", callback_data="8")
btn9 = types.InlineKeyboardButton("9", callback_data="9")
btn10 = types.InlineKeyboardButton("10", callback_data="10")
btn11 = types.InlineKeyboardButton("11", callback_data="11")
btn12 = types.InlineKeyboardButton("12", callback_data="12")
btn13 = types.InlineKeyboardButton("13", callback_data="13")
btn14 = types.InlineKeyboardButton("14", callback_data="14")
btn15 = types.InlineKeyboardButton("15", callback_data="15")
btn16 = types.InlineKeyboardButton("16", callback_data="16")
btn17 = types.InlineKeyboardButton("17", callback_data="17")
btn18 = types.InlineKeyboardButton("18", callback_data="18")
btn19 = types.InlineKeyboardButton("19", callback_data="19")
btn20 = types.InlineKeyboardButton("20", callback_data="20")
inline_keyboard.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Привет, парсим категорию - ВСЕ НОВОСТИ: ")
    count_ = 0
    if len(title_)==0:
         bot.send_message(chat_id,"На сегодняшний день пока новостей еще нет ")
    for i in title_:
        count_ += 1
        bot.send_message(chat_id, str(count_) + i)

    bot.send_message(chat_id,"Какую новость показать подробней? ", reply_markup=inline_keyboard)



@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data=='1':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='2':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='3':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='4':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='5':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='6':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='7':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='8':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='9':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='10':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='11':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='12':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='13':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='14':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='15':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='16':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='17':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='18':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='19':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if c.data=='20':
        chat_id=c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    k1 = types.KeyboardButton('Description')
    k2 = types.KeyboardButton('Photo')
    k3 = types.KeyboardButton('Quit')
    income_keyboard.add(k1,k2,k3)
    global msg
    msg = bot.send_message(chat_id,"some title news you can see Description of this news and Photo",reply_markup=income_keyboard)
    bot.register_next_step_handler(msg,get_category_income)
    global inf
    inf = int(c.data)-1
    


def get_category_income(message):
    chat_id=message.chat.id
    entry = message.text
    if entry == "Description":
        try:
            bot.send_message(chat_id, big_title[inf])
            bot.register_next_step_handler(msg,get_category_income)
        except:
            bot.send_message(chat_id,"Новостей пока нет")
    if entry == "Photo":
        try:
            bot.send_message(chat_id, list_img[inf])
            bot.register_next_step_handler(msg,get_category_income)
        except:
            bot.send_message(chat_id,"Новостей пока нет")
    if entry == "Quit":
        bot.send_message(chat_id,"До свидания")


bot.polling()