import telebot, os

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=["start"])
def s(m):
    bot.send_message(m.chat.id, "✅ bot is online")

print("Bot started...")
bot.infinity_polling()
