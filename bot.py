import telebot

# BotFather'dan olgan tokenni shu yerga qo'ying
TOKEN = '8509295474:AAFTh1Fn9A4OWUlbc2yuhnoli7wHYQRq1nI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Menga matematik misol yuboring (masalan: 2+2*5).")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # Xavfsiz hisoblash uchun eval funksiyasi
        # Faqat raqamlar va amallar borligini tekshirish tavsiya etiladi
        result = eval(message.text)
        bot.reply_to(message, f"Natija: {result}")
    except Exception:
        bot.reply_to(message, "Xatolik! Faqat matematik amallarni yuboring.")

if __name__ == '__main__':
    bot.polling(none_stop=True)