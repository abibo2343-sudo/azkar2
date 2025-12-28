# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os
from azkar import AZKAR

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ============ Keyboards ============
def main_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🌅 أذكار الصباح", callback_data="morning"),
        InlineKeyboardButton("🌇 أذكار المساء", callback_data="evening"),
        InlineKeyboardButton("🌙 أذكار النوم", callback_data="sleep"),
        InlineKeyboardButton("🕌 بعد الصلاة", callback_data="prayer"),
    )
    return kb

# ============ Handlers ============
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(
        m.chat.id,
        "📿 *بوت أذكار المسلم*\nاختر نوع الذكر:",
        reply_markup=main_kb()
    )

@bot.callback_query_handler(func=lambda c: True)
def handle(c):
    key = c.data
    if key in AZKAR:
        zekr = random.choice(AZKAR[key])
        bot.send_message(
            c.message.chat.id,
            f"📿\n\n{zekr}",
            reply_markup=main_kb()
        )
    bot.answer_callback_query(c.id)

# ============ Run ============
print("📿 Azkar Bot is running...")
bot.infinity_polling(skip_pending=True)
