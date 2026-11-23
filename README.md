# Shop Parser

Сервис парсит товары из интернет-магазина, сохраняет их в базу данных и отдаёт клиенту через веб-интерфейс.

## Стек

- **beautifulsoup4** — парсинг HTML
- **requests** — HTTP-запросы к магазину
- **SQLAlchemy** — ORM и работа с базой данных
- **FastAPI** — REST API и веб-выдача данных
- **uvicorn** — ASGI-сервер

## Как это работает

1. Парсер запрашивает страницы каталога магазина через `requests`.
2. `beautifulsoup4` извлекает из HTML название, цену, описание, изображение и ссылку на товар.
3. Данные сохраняются в БД через SQLAlchemy. Повторные товары обновляются, а не дублируются.
4. FastAPI отдаёт данные из БД клиенту, веб-страница их отображает.

## Структура проекта

      .├── app/│   ├── main.py          # FastAPI-приложение, эндпоинты│   ├── models.py        # SQLAlchemy-модели│   ├── database.py      # подключение к БД, сессии│   └── schemas.py       # Pydantic-схемы ответов API├── parser/│   ├── scraper.py       # загрузка страниц через requests│   ├── extractor.py     # извлечение данных через BeautifulSoup│   └── run.py           # точка входа парсера├── static/              # фронтенд (HTML/CSS/JS)├── requirements.txt├── .env.example└── README.md

          
            
            
          
          
## Требования

- Python 3.10+
- PostgreSQL или SQLite (по умолчанию SQLite)

## Установка

```bash
git clone <repo-url>
cd <project-dir>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
      Настройка
Скопируйте файл с примером переменных окружения и при необходимости измените значения:

          
            
            
          
          cp .env.example .env
      


Переменная
Описание
Пример



DATABASE_URL
строка подключения SQLAlchemy
sqlite:///./shop.db


SHOP_BASE_URL
адрес магазина, откуда парсятся товары
https://example-shop.com


PARSER_DELAY
пауза между запросами к магазину, в секундах
1.0


USER_AGENT
User-Agent для запросов
Mozilla/5.0 (compatible; ShopParser)


Секреты и строки подключения храните только в .env. Файл .env не должен попадать в git.
Запуск
1. Создание таблиц

          
            
            
          
          python -m app.database
      2. Запуск парсера

          
            
            
          
          python -m parser.run
      Парсер обходит каталог, извлекает товары и записывает их в БД. Задержка между запросами берётся из PARSER_DELAY.
3. Запуск веб-сервера

          
            
            
          
          uvicorn app.main:app --reload
      Сайт доступен по адресу http://127.0.0.1:8000.
API



Метод
Путь
Описание



GET
/
веб-страница со списком товаров


GET
/api/products
список товаров (пагинация)


GET
/api/products/{id}
карточка товара


Документация Swagger доступна на /docs.
Пример ответа GET /api/products?limit=2:

          
            
            
          
          [
  {
    "id": 1,
    "name": "Беспроводная мышь",
    "price": 1490.0,
    "currency": "RUB",
    "url": "https://example-shop.com/product/123",
    "image_url": "https://example-shop.com/img/123.jpg",
    "updated_at": "2026-11-23T10:00:00Z"
  }
]
      Параметры пагинации: limit (по умолчанию 20), offset (по умолчанию 0).
Модель данных
Таблица products:



Поле
Тип
Описание



id
Integer PK
внутренний идентификатор


external_id
String, UNIQUE
идентификатор товара в магазине


name
String
название


price
Numeric
цена


currency
String(3)
код валюты


url
String
ссылка на товар в магазине


image_url
String
ссылка на изображение


updated_at
DateTime
время последнего обновления


Важно перед использованием

Проверьте robots.txt и условия использования магазина. Парсинг допустим только там, где он разрешён.
Соблюдайте паузу между запросами, чтобы не нагружать сервер магазина.
Если магазин отдаёт данные через JavaScript, requests и BeautifulSoup их не увидят. В этом случае понадобится другой инструмент (например, Playwright).

Разработка
Запуск с автоперезагрузкой:

          
            
            
          
          uvicorn app.main:app --reload
      Для повторного полного обхода каталога достаточно снова запустить python -m parser.run. Уже сохранённые товары обновятся по external_id.
Лицензия
Укажите лицензию проекта.

          
            
            
          
          
Что нужно уточнить, чтобы README стал точным:
1. Какой магазин парсится, и отдаёт ли он HTML без JavaScript?
2. Используете ли вы SQLite или PostgreSQL?
3. Фронтенд — это статические файлы, шаблоны Jinja2 или отдельное SPA?
4. Нужно ли запускать парсер по расписанию (cron, APScheduler)? Тогда добавлю раздел об этом.
