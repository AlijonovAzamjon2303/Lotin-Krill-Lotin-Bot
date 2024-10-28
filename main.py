from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '6542995913:AAHoafmHxnCXrqo1K8nmOgouuMdozlq6XNE'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

matn = input("Matn kiriting : ")

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))