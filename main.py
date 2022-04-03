# coding: utf-8

import telebot
import config
import asyncio
import aiohttp
from aiohttp import web
import json

from telebot import types
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Время старта программы =", current_time)

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start12345(message):

  bot.send_message(message.chat.id, 'Трендовые вещи с ОТЛИЧНОЙ ЦЕНОЙ здесь.\n🔥ОПТ|РОЗНИЦА🔥\n\n✅Отличное качество всех товаров\n✅Предоставляем лучшие цены\n✅Полная поддержка наших клиентов ( обмен брака) \n✅Оформление и отправка в день заказа', reply_markup=menu)

def qwerty(message):
	bot.send_message(message.chat.id, 'Трендовые вещи с ОТЛИЧНОЙ ЦЕНОЙ здесь.\n🔥ОПТ|РОЗНИЦА🔥\n\n✅Отличное качество всех товаров\n✅Предоставляем лучшие цены\n✅Полная поддержка наших клиентов ( обмен брака) \n✅Оформление и отправка в день заказа')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
        	################################ MENU #######################################
            if call.data == 'katalog':
                bot.send_message(call.message.chat.id, '⚡️Прайс⚡️\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=katalog)
                print('KATALOG отправилось!')
            elif call.data == 'prochee':
                bot.send_message(call.message.chat.id, 'По вопросам и ошибкам бота пишите сюда: @My_goodness00', reply_markup=prochee)
                print('PROCHEE отправилось!')
            ################################ MENU #######################################


            ############################### KATALOG #####################################
            elif call.data == 'odnorazki':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
                print('ODNORAZKI отправилось!')
            elif call.data == 'pod':
                bot.send_message(call.message.chat.id, 'Это пока что не доступно:)', reply_markup=pod, parse_mode="html")
                print('POD отправилось!')
            elif call.data == 'jija':
                bot.send_message(call.message.chat.id, 'Это пока что не доступно:)', reply_markup=jija, parse_mode="html")
                print('JIJA отправилось!')
            elif call.data == 'ispariki':
                bot.send_message(call.message.chat.id, 'Это пока что не доступно:)', reply_markup=ispariki, parse_mode="html")
                print('ISPARIKI отправилось!')
            elif call.data == 'exit1':
                bot.send_message(call.message.chat.id, 'Трендовые вещи с ОТЛИЧНОЙ ЦЕНОЙ здесь.\n🔥ОПТ|РОЗНИЦА🔥\n\n✅Отличное качество всех товаров\n✅Предоставляем лучшие цены\n✅Полная поддержка наших клиентов ( обмен брака) \n✅Оформление и отправка в день заказа', reply_markup=menu)
            ############################### KATALOG #####################################


            ############################## ODNORAZKI ####################################
            elif call.data == 'exit2':
            	bot.send_message(call.message.chat.id, '⚡️Прайс⚡️\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=katalog, parse_mode="html")
            elif call.data == 'izi':
                bot.send_message(call.message.chat.id, '<b>Вкусы:\n\nIZI MAX (550 руб)\n\n🍈Дыня🍈\n🍓Клубника, арбуз🍉\n🍏Яблоко, банан🍌\n🍓Клубника🍓\n🍋Лайм, махито🍸\n🍹Розовый лимонад🍹\n🍇Чирника🍇\n🍋Цитрус🍋\n🍐Гуава, арбуз🍉\n🍉Манга, лёд🧊\n☕️Молочный чай☕️\n🍦Ванильное мороженое🍦\n🍈Микс вкусов🍓\n\nПо наличию обращаться: @My_goodness00</b>', reply_markup=izi, parse_mode="html")
                print('IZI отправилось!')
            elif call.data == 'elfbar':
                bot.send_message(call.message.chat.id, '<b>Вкусы:\n\nElfBar Lux (500 руб)\n\n🍇Черника🍇\n🍹Пиноколада🍹\n🥤Кола🥤\n🥝Киви, цитрус, гуава🍐\n🥭Манго🥭\n🥃Блюраз🥃\n🍍Ананас, персик, манго🥭\n🍹Розовый лимонад🍹\n🌧Неоновый дождь🌧\n🍉Арбуз🍉\n🍓Клубника, мороженое🍦\n🍎Яблоко, персик🍑\n🍇Виноград🍇\n🍌Банан, лёд🧊\n🥥Кокос, дыня🍈\n\nПо наличию обращаться: @My_goodness00</b>', reply_markup=elfbar, parse_mode="html")
                print('ElfBar отправилось!')
            elif call.data == 'dormi':
                bot.send_message(call.message.chat.id, '<b>Вкусы:\n\nDormi (700 руб)\n\n🍊Ягода личи🍊\n🥭Манго, лёд🧊\n🍐Смешанные фрукты🍎\n🍓Клубника, киви🥝\n\nПо наличию обращаться: @My_goodness00</b>', reply_markup=dormi, parse_mode="html")
                print('DORMI отправилось!')
            elif call.data == 'toomi':
                bot.send_message(call.message.chat.id, 'Пока что нет в наличии:)', reply_markup=toomi, parse_mode="html")
                print('TOOMI отправилось!')
            elif call.data == 'hqd':
                bot.send_message(call.message.chat.id, '<b>Вкусы:\n\nHQD (Старая Упаковка) (450 руб)\n\n🧃Гранатовый сок, смородина, лимон🍋\n🍓Малина, лимон🍋\n🍓Клубника, банан🍌\n🥭Манго🥭\n🥬Жвачка, мята🥬\n🍉Арбуз🍉\n🍈Дыня🍈\n🍓Клубника🍓\n🍉Арбуз, клубника🍓\n🍇Чёрная смородина🍇\n🍏Яблоко, персик🍑\n🍍Ананас🍍\n💨Туманы💨\n🌊Майями🌊\n🍌Банан🍌\n🥭Манго, гуава🍐\n🍇Йогурт, лесные ягоды🍓\n🍊Мультифрукт🍐\n\nПо наличию обращаться: @My_goodness00</b>', reply_markup=hqd, parse_mode="html")
                print('HQD отправилось!')
            #elif call.data == 'dormi2':
                #bot.send_message(call.message.chat.id, 'sjfksdaflsdjflksad;flkajsdfkjasdf;lkjads;flkj;l', reply_markup=dormi2, parse_mode="html")
                #print('DORMI2 отправилось!')
            elif call.data == 'sky':
                bot.send_message(call.message.chat.id, 'Пока что нет в наличии:)', reply_markup=sky, parse_mode="html")
                print('SKY MOON отправилось!')
            elif call.data == 'city':
                bot.send_message(call.message.chat.id, 'Пока что нет в наличии:)', reply_markup=city, parse_mode="html")
                print('CITY отправилось!')
            #elif call.data == 'hqd2':
                #bot.send_message(call.message.chat.id, 'sjfksdaflsdjflksad;flkajsdfkjasdf;lkjads;flkj;l', reply_markup=hqd2, parse_mode="html")
                #print('HQD2 отправилось!')
            ############################## ODNORAZKI ####################################



            ############################## PROCHEE ######################################
            elif call.data == 'exit4':
            	bot.send_message(call.message.chat.id, 'Трендовые вещи с ОТЛИЧНОЙ ЦЕНОЙ здесь.\n🔥ОПТ|РОЗНИЦА🔥\n\n✅Отличное качество всех товаров\n✅Предоставляем лучшие цены\n✅Полная поддержка наших клиентов ( обмен брака) \n✅Оформление и отправка в день заказа', reply_markup=menu, parse_mode="html")
            ############################## PROCHEE ######################################



            ############################## POD ######################################
            elif call.data == 'exit5':
            	bot.send_message(call.message.chat.id, '⚡️Прайс⚡️\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=katalog, parse_mode="html")
            ############################## POD ######################################



            ############################## JIJA ######################################
            elif call.data == 'exit6':
            	bot.send_message(call.message.chat.id, '⚡️Прайс⚡️\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=katalog, parse_mode="html")
            ############################## JIJA ######################################



            ############################## ISPARIKI ######################################
            elif call.data == 'exit7':
            	bot.send_message(call.message.chat.id, '⚡️Прайс⚡️\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=katalog, parse_mode="html")
            ############################## ISPARIKI ######################################



            #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_ MARKUP ODNORAZKI #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
            ############################## IZI ###########################################
            elif call.data == 'exit8':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## IZI ###########################################



            ############################## ElfBar ###########################################
            elif call.data == 'exit9':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## ElfBar ###########################################



            ############################## HQD1 ###########################################
            elif call.data == 'exit10':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## HQD1 ###########################################



            ############################## TOOMI ###########################################
            elif call.data == 'exit11':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## TOOMI ###########################################



            ############################## DORMI1 ###########################################
            elif call.data == 'exit12':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## DORMI1 ###########################################



            ############################## HQD2 ###########################################
            elif call.data == 'exit13':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## HQD2 ###########################################



            ############################## DORMI2 ###########################################
            elif call.data == 'exit14':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## DORMI2 ###########################################



            ############################## SKYMOON ###########################################
            elif call.data == 'exit15':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## SKYMOON ###########################################



            ############################## CITY ###########################################
            elif call.data == 'exit16':
                bot.send_message(call.message.chat.id, '🔥Каталог Одноразок🔥\n\n\nЕсть вопросы по товару, пишите сюда: @My_goodness00', reply_markup=odnorazki, parse_mode="html")
            ############################## CITY ###########################################

            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
            print(repr(e))


############################################ VEBHOOK ##############################################
async def init_app(loop):
    app = web.Application(loop=loop, middlewares=[])
    app.router.add_post('/api/v1', handler)
    return app

async def handler(request):
    data = await request.json()
    headers = {
        'Content-Type': 'application/json'
    }
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': data['message']['text']
    }
############################################ VEBHOOK ##############################################



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
buttonB = types.InlineKeyboardButton('ElfBar Lux', callback_data='elfbar')
buttonC = types.InlineKeyboardButton('Toomi', callback_data='toomi') 
buttonD = types.InlineKeyboardButton('Dormi', callback_data='dormi')
buttonW = types.InlineKeyboardButton('HQD(старая упаковка)', callback_data='hqd')
#buttonE = types.InlineKeyboardButton('Dormi', callback_data='dormi2')
buttonR = types.InlineKeyboardButton('SKY MOON', callback_data='sky')
buttonT = types.InlineKeyboardButton('City', callback_data='city')
#buttonQ = types.InlineKeyboardButton('HQD(новая упаковка)', callback_data='hqd2')
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit2')

odnorazki.row(buttonA, buttonB)#, buttonQ
odnorazki.row(buttonC, buttonD, buttonW)
odnorazki.row(buttonR, buttonT)#buttonE,
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


########################################## ISPARIKI #############################################
ispariki = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit7')

ispariki.row(buttonY)
########################################## ISPARIKI #############################################



#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_ MARKUP ODNORAZKI #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_
########################################## IZI MAX #############################################
izi = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit8')

izi.row(buttonY)
########################################## IZI MAX #############################################

########################################## ElfBar #############################################
elfbar = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit9')

elfbar.row(buttonY)
########################################## ElfBar #############################################

########################################## HQD1 #############################################
hqd = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit10')

hqd.row(buttonY)
########################################## HQD1 #############################################

########################################## TOOMI #############################################
toomi = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit11')

toomi.row(buttonY)
########################################## TOOMI #############################################

########################################## DORMI1 #############################################
dormi = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit12')

dormi.row(buttonY)
########################################## DORMI1 #############################################

########################################## HQD2 #############################################
hqd2 = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit13')

hqd2.row(buttonY)
########################################## HQD2 #############################################

########################################## DORMI2 #############################################
dormi2 = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit14')

dormi2.row(buttonY)
########################################## DORMI2 #############################################

########################################## SKYMOON #############################################
sky = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit15')

sky.row(buttonY)
########################################## SKYMOON #############################################

########################################## CITY #############################################
city = types.InlineKeyboardMarkup()
buttonY = types.InlineKeyboardButton('<=====Назад', callback_data='exit16')

city.row(buttonY)
########################################## CITY #############################################

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_ MARKUP Jija #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_ MARKUP Jija #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_ MARKUP ODNORAZKI #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_



########################################### MARKUP #############################################
bot.polling (none_stop=True)

############################################ VEBHOOK ##############################################
app = loop.run_until_complete(init_app(loop))
web.run_app(app, host='0.0.0.0', port=23456)
############################################ VEBHOOK ##############################################

#🔥!!!В продаже офигенные одноразки по хорошим ценам!!!!🔥

#🔥💨1. IZI MAX 1600 тяг - 550 руб💨🔥
#🔥💨2. HQD 1200 тяг - 450 руб💨🔥

#По вкусам и наличию пишите 😏My_goodness00 (telegram) или 🤖candy_shop_1bot (telegram bot)