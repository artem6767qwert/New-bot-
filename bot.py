import os
import telebot
import requests

# Получаем токен Telegram бота из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # ID канала для отправки скидок

bot = telebot.TeleBot(BOT_TOKEN)

# Функция для парсинга скидок (пример с заглушкой)
def get_discounts():
    discounts = [
        {"name": "Смартфон Samsung", "price": 19999, "old_price": 25999, "link": "https://ozon.ru"},
        {"name": "Ноутбук ASUS", "price": 54999, "old_price": 65999, "link": "https://wildberries.ru"},
    ]
    return discounts

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я помогу тебе найти лучшие скидки на маркетплейсах!")

# Команда /sales
@bot.message_handler(commands=['sales'])
def send_sales(message):
    discounts = get_discounts()
    for item in discounts:
        discount_text = f"🔥 {item['name']}\n💰 Цена: {item['price']} ₽ (Старая: {item['old_price']} ₽)\n🔗 {item['link']}"
        bot.send_message(message.chat.id, discount_text)

# Автоматическая отправка скидок в канал
def send_discounts_to_channel():
    discounts = get_discounts()
    for item in discounts:
        discount_text = f"🔥 {item['name']}\n💰 Цена: {item['price']} ₽ (Старая: {item['old_price']} ₽)\n🔗 {item['link']}"
        bot.send_message(CHANNEL_ID, discount_text)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
