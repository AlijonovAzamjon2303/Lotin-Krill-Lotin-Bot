from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "6542995913:AAGeG2dfcuZJ6tSZ6ShTy-KjSgWm01tqSuk"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)

bot.polling()

# matn = input("Matn kiriting : ")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))