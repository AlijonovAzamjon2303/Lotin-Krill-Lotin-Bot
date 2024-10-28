from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "Bu yerga Botingizni Tokenini joylashtirsiz"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)

@bot.message_handler(func = lambda msg : msg.text is not None)
def trnslit(message):
    msg = message.text
    javob = lambda msg : to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()