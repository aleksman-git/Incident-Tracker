Маленький API-сервис для учёта инцидентов

#### 1. Создайте пользователя и базу данных в PostgreSQL:
CREATE ROLE "user" WITH LOGIN NOINHERIT CREATEDB PASSWORD 'user';
CREATE DATABASE itracker WITH OWNER = "user" ENCODING = 'UTF8';

#### 2. Создайте виртуальное окружение и установите библиотеки
Установка библиотек с помощью файла requirements.txt
```sh
pip install -r requirements.txt
```
# Удалите старые миграции и создайте новые
```sh
python manage.py makemigrations
```
# Примените миграции
```sh
python manage.py migrate
```
# Запустите сервер
```sh
python manage.py runserver
```