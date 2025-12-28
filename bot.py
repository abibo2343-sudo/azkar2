import telebot, os, time

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def s(m):
    bot.send_message(m.chat.id, "✅ BOT IS ONLINE")

print("Bot started...")
bot.infinity_polling()
