import json
import time
from datetime import datetime

import requests
import telebot


# получение config
def getting_config():
    with open(f'Data/config.txt', 'r', encoding='utf-8') as file:
        config = []
        config.append(file.readline().strip().split(":", 1)[1])
        config.append(file.readline().strip().split(":", 1)[1])
        config.append(file.readline().strip().split(":", 1)[1])
    return config


# получение параметров запроса
def getting_params():
    with open(f'Data/params.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        return json.loads(data)


def log(message, ConsolePrint=True, FileWrite=True, TelegramMessage=True):
    if ConsolePrint:
        print(f'[{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}] {message}')

    if FileWrite:
        with open(f'Data/log.txt', 'a', encoding='utf-8') as file:
            file.write(f'[{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}] {message}\n')

    if TelegramMessage:
        bot.send_message(USER_ID, message)


# уведомление пользователей о появлении новых аккаунтов
def send_messages(title, price, link_acc, item_id):
    log(f"Отправка уведомления о аккаунту {title}", TelegramMessage=False)
    bot.send_message(USER_ID, f"Название: {title}\n"
                              f"Цена: {price}\n"
                              f"Ссылка steam: {link_acc}\n"
                              f"Ссылка на аакаунт: https://lolz.guru/market/{item_id}/")


# бронирование аккаунтов
def booking_accounts(item_id, price, title):
    log(f"Бронирование аккаунта {title}", TelegramMessage=False)
    r = requests.get(f"https://api.lolz.guru/market/{item_id}/reserve?oauth_token={token}",
                      params={"price": price})
    if r.status_code == 200:
        log(f"Аккаунт {title} забронирован")
    else:
        log(f"Ошибка при бронировании аккаунта {title}")


def main():
    global real_time, t, params
    items = requests.get(url, params=params).json()["items"]
    for acc in items[:20]:

        if real_time < acc["published_date"]:

            if acc["published_date"] > t:
                t = acc["published_date"]

            link_acc = acc["accountLink"]
            item_id = acc["item_id"]
            price = acc["price"]
            title = acc["title"]

            send_messages(title, price, link_acc, item_id)
            booking_accounts(item_id, price, title)

    if t > real_time:
        real_time = t
    time.sleep(3)


real_time = time.time()
t = 0
params = getting_params()
token, API_KEY, USER_ID = getting_config()
bot = telebot.TeleBot(API_KEY)
log(f"Парсер начал работу")
url = f"https://api.lolz.guru/market/steam?oauth_token={token}"

while True:
    log("Запрос на новые аккаунты", TelegramMessage=False)
    try:
        main()
    except Exception as ex:
        log(ex, TelegramMessage=False)
        time.sleep(20)
        main()

