## parser-bot-guru
Telegram-bot, которпый парсит сайт https://zelenka.guru/ уведомляет пользователей о появлениии новых аккаунтов и блокирует их по указанным пареаментрам.

## Как запустить
1. В файле config.txt указать
* свой токен на сайте https://zelenka.guru/
* указть токен для бота
* указать ваш ID в telegram

    Пример
    ```
    token_guru:<YOUR token>
    API_KEY_Telegram:<BOT token>
    USER_ID_Telegram:<YOUR ID tg>
    ```
2. Указать параметры запросов

    Пример
    ```
    {
    "pmin": 200,
    "pmax": 450,
    "game[]": 730,
    "origin[]": "brute",
    "no_vac": 1,
    "recently_hours_max": 0,
    "order_by": "pdate_to_down"
    }
    ```
3. Запустить бота
