import requests
import telepot
from random import randint
from bs4 import BeautifulSoup
from telepot.loop import MessageLoop
from unicodedata import normalize

token = '791343877:AAGTLHGSGK6Ga5_zppQi9c9PMvEK26O0b7k'
bot = telepot.Bot(token)
msg = bot.getUpdates()
print("Bot iniciado!")

# RASPAGEM DE GIFS

def raspa(busca,chatID):
    url = 'https://giphy.com/search/' + busca
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    gifs = soup.findAll('img', class_='gif_gifImage__3dFjs gif_gifLink__TKut_')
    num = randint(1,30) #REALIZA UM SORTEIO ENTRE OS 30 PRIMEIROS GIFS DA BUSCA
    count = 0
    for gif in gifs:
        count += 1
        imagem = gif['src']
        if count == num:
            bot.sendPhoto(chatID, imagem)
            
# TRATAMENTO DAS MENSAGENS E CRIAÇÃO DO LOG

def defaul(msg):
    chatID = msg['chat']['id']
    nome = msg['chat']['first_name']
    sobrenome = msg['chat']['last_name']
    mensagem = (msg['text'])
    mensagem = mensagem.lower()
    mensagem = normalize('NFKD', mensagem).encode('ASCII', 'ignore').decode('ASCII')
    print('[',chatID,']',nome,sobrenome,':',msg['text'])
    if('/gif ' in mensagem): # FAZ A CHAMADA NO TELEGRAM PARA BUSCAR O GIF
        busca = msg['text'].lower().replace('/gif ','')
        raspa(busca,chatID)

# MANTEM O BOT RODANDO

bot.message_loop(defaul)
while True:
    pass
