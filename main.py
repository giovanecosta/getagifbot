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

def inicio(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id, "Oi! Eu sou o PullBot!\nQual o título da enquete que você quer abrir?")

def enquete(msg):   
        content_type, chat_type, chat_id = telepot.glance(msg)
        texto = msg['text']
        bot.sendMessage(chat_id, texto)

def opcoes(msg):
        if msg.lower() == "opções":
                coletando = 0
                while coletando == 0:
                        content_type, chat_type, chat_id = telepot.glance(msg)
                        opc = []
                        opc.append(msg['text'])
                        if msg.lower() == "fim":
                                coletando = 1
                                apc.pop(-1)
        for i in opc:
                bot.sendMessage(chat_id, i)

# Mantém o bot em escuta o tempo todo
bot.message_loop(
    {
        'chat': opcoes,
    }
)

print ('Listening ...')
while 1:
    time.sleep(3)
