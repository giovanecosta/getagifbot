import requests,commands,json,time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import (ForceReply, InlineKeyboardButton,
                                InlineKeyboardMarkup, InlineQueryResultArticle,
                                InputTextMessageContent, KeyboardButton,
                                ReplyKeyboardMarkup)

token = '703302532:AAFAJKCE9ZfnX9xf2Bdb6i88JWLbL0JXAIs'
bot = telepot.Bot(token)
msg = bot.getUpdates()
cmd = commands.Commands(token)

def inicio(msg1):
        content_type, chat_type, chat_id = telepot.glance(msg1)
        cmd.getCommand(msg1,chat_id)
        

def on_callback_query(msg2):
        data = msg2
        print(data)

if __name__ == "__main__":
        print("Servidor on...")
        MessageLoop(bot, {
                "chat": inicio,
                "callback_query": on_callback_query
        }).run_as_thread()
        while 1:
                try:
                        time.sleep(3)
                        pass
                except:
                        break
