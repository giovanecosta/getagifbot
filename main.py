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
        print(content_type, chat_type, chat_id)
        bot.sendMessage(chat_id, "No Hadadd! É claro!")
        saida = 1

def criarEnquete(msg):   
        content_type, chat_type, chat_id = telepot.glance(msg)
        texto = msg['text']
        bot.sendMessage(chat_id, "Essa é sua pergunta:")
        bot.sendMessage(chat_id, texto)
        saida = 1

# Mantém o bot em escuta o tempo todo
bot.message_loop(
    {
        'chat': inicio,
        'callback_query': criarEnquete,
    }
)

print ('Listening ...')
while True:
    pass
