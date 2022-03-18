import telebot
import config

from telebot import types
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Время старта программы =", current_time)

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start12345(message):

  bot.send_message(message.chat.id, 'Здравствуйте, я бот ..., вам нужна помащь?', reply_markup=menu)

def qwerty(message):
	bot.send_message(message.chat.id, 'Здравствуйте, я бот ..., вам нужна помащь?')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
        	################################ MENU #######################################
            if call.data == 'katalog':
                bot.send_message(call.message.chat.id, 'Каталог:', reply_markup=katalog)
            elif call.data == 'prochee':
                bot.send_message(call.message.chat.id, 'Это пока что не доступно:)', reply_markup=prochee)
            ################################ MENU #######################################


            ############################### KATALOG #####################################
            elif call.data == 'odnorazki':
                bot.send_message(call.message.chat.id, 'ассортимент:', reply_markup=odnorazki, parse_mode="html")
            elif call.data == 'pod':
                bot.send_message(call.message.chat.id, 'Это пока что не доступно:)', reply_markup=pod, parse_mode="html")
            elif call.data == 'jija':
                bot.send_message(call.message.chat.id, 'Это пока что не доступно:)', reply_markup=jija, parse_mode="html")
            elif call.data == 'ispariki':
                bot.send_message(call.message.chat.id, 'Это пока что не доступно:)', reply_markup=ispariki, parse_mode="html")
            elif call.data == 'exit1':
                bot.send_message(call.message.chat.id, 'Здравствуйте, я бот ..., вам нужна помащь?', reply_markup=menu)
            ############################### KATALOG #####################################


            ############################## ODNORAZKI ####################################
            elif call.data == 'exit2':
            	bot.send_message(call.message.chat.id, 'Каталог:', reply_markup=katalog, parse_mode="html")
            ############################## ODNORAZKI ####################################



            ############################## PROCHEE ######################################
            elif call.data == 'exit4':
            	bot.send_message(call.message.chat.id, 'Здравствуйте, я бот ..., вам нужна помащь?', reply_markup=menu, parse_mode="html")
            ############################## PROCHEE ######################################



            ############################## POD ######################################
            elif call.data == 'exit5':
            	bot.send_message(call.message.chat.id, 'Каталог:', reply_markup=katalog, parse_mode="html")
            ############################## POD ######################################



            ############################## JIJA ######################################
            elif call.data == 'exit6':
            	bot.send_message(call.message.chat.id, 'Каталог:', reply_markup=katalog, parse_mode="html")
            ############################## JIJA ######################################



            ############################## ISPARIKI ######################################
            elif call.data == 'exit7':
            	bot.send_message(call.message.chat.id, 'Каталог:', reply_markup=katalog, parse_mode="html")
            ############################## ISPARIKI ######################################

            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
            print(repr(e))


############################################## MARKUP #############################################
############################################## KATALOG ############################################
katalog = types.InlineKeyboardMarkup()
buttonA = types.InlineKeyboardButton('Одноразки', callback_data='odnorazki')
buttonB = types.InlineKeyboardButton('Поды', callback_data='pod')
buttonC = types.InlineKeyboardButton('Жижи', callback_data='jija') 
buttonD = types.InlineKeyboardButton('Испарики', callback_data='ispariki')
buttonE = types.InlineKeyboardButton('<===Назад', callback_data='exit1')

katalog.row(buttonA, buttonB)
katalog.row(buttonC, buttonD, buttonE)
############################################## KATALOG ############################################



############################################## MENU ###############################################
menu = types.InlineKeyboardMarkup()
buttonA = types.InlineKeyboardButton('Каталог', callback_data='katalog')
buttonB = types.InlineKeyboardButton('Прочее', callback_data='prochee')

menu.row(buttonA, buttonB)
############################################## MENU ###############################################



############################################ ODNORAZKI ############################################
odnorazki = types.InlineKeyboardMarkup()
buttonA = types.InlineKeyboardButton('IZI MAX', callback_data='izi')
buttonB = types.InlineKeyboardButton('ElfBar', callback_data='elfbar')
buttonC = types.InlineKeyboardButton('Toomi', callback_data='toomi') 
buttonD = types.InlineKeyboardButton('Dormi', callback_data='dormi')
buttonW = types.InlineKeyboardButton('HQD', callback_data='hqd')
buttonE = types.InlineKeyboardButton('Dormi', callback_data='dormi') 
buttonR = types.InlineKeyboardButton('SKY MOON', callback_data='sky')
buttonT = types.InlineKeyboardButton('City', callback_data='city')
buttonQ = types.InlineKeyboardButton('HQD', callback_data='hqd')
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit2')

odnorazki.row(buttonA, buttonB, buttonQ)
odnorazki.row(buttonC, buttonD, buttonW)
odnorazki.row(buttonE, buttonR, buttonT)
odnorazki.row(buttonY)
############################################ ODNORAZKI ############################################



############################################# PROCHEE #############################################
prochee = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit4')

prochee.row(buttonY)
############################################# PROCHEE #############################################



############################################# POD #############################################
pod = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit5')

pod.row(buttonY)
############################################# POD #############################################



############################################# JIJA #############################################
jija = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit6')

jija.row(buttonY)
############################################# JIJA #############################################


############################################# ISPARIKI #############################################
ispariki = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit7')

ispariki.row(buttonY)
############################################# ISPARIKI #############################################
############################################## MARKUP #############################################
bot.polling (none_stop=True)