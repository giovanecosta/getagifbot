import telepot
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import (ForceReply, InlineKeyboardButton,
                                InlineKeyboardMarkup, KeyboardButton,
                                ReplyKeyboardMarkup, InlineQueryResultArticle, 
                                InputTextMessageContent)

token = '667895949:AAFa5ic_yU0boRWKCh5EKe7vlE08fjAHQYM'
bot = telepot.Bot(token)
msg = bot.getUpdates()
global saida
saida = 0

def inicio(msg):
    global saida
    if(saida == 0):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        bot.sendMessage(chat_id, "Olá!\nEu sou o PullBot.\n"
                                "Qual a pergunta que você gostaria de fazer?")
        nome = InputTextMessageContent()
        saida = 1

def criarEnquete(msg):
    global saida
    if(saida == 0):    
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        bot.sendMessage(chat_id, "text")
        saida = 1

# Mantém o bot em escuta o tempo todo
MessageLoop(bot, inicio).run_as_thread()
print ('Listening ...')
while 1:
    time.sleep(10)
