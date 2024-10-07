# Notifications_FastApi

Проект написан на FastApi 0.112.2
Сервис для оплаты товаров на сайте

## Установка

1. Клонировать репозиторий

```bash
git clone https://github.com/AndyRetroWave/Devisions_Notifications_FastApi.git
```

2. Установить зависимости

```bash
poetry shell
poetry install
```

3. Создать файл .env и добавить в него переменные окружения

```bash
DB_USER=<username>
DB_PASS=<password>
DB_HOST=<host>
DB_PORT=<port>
DB_NAME=<database_name>
```

4. Запустить проект

```bash
uvicorn main:app --reload
```

Установка через docker-compose

```bash
docker-compose up -d
```
