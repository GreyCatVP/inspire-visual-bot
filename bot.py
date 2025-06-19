import telebot
from ai_visual_helper import get_visual_inspiration
import os
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Я бот для визуального вдохновения. Напиши тему — и я пришлю тебе референсы.\n\nПример: coffee packaging")

@bot.message_handler(func=lambda m: True)
def handle_query(message):
    query = message.text.strip().lower()
    results = get_visual_inspiration(query)

    if not results:
        bot.send_message(message.chat.id, "😕 Пока нет вдохновения по этой теме. Попробуй другую.")
        return

    for item in results:
        caption = f"\ud83d\udcc4 <b>{item['title']}</b>\n\n\ud83e\udde0 {item['description']}\n\n\ud83d\udd17 <a href='{item['link']}'>Смотреть на Behance</a>"
        bot.send_photo(message.chat.id, item['image'], caption=caption, parse_mode='HTML')

if __name__ == '__main__':
    bot.polling(none_stop=True)
