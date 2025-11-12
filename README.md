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
REST API swagger будет доступна по адресу:
http://127.0.0.1:8000/swagger/

Примеры работы:
<img width="980" height="620" alt="image" src="https://github.com/user-attachments/assets/030f4a44-1a24-4b1a-8e71-16dd2eb9a7ca" />

<img width="964" height="594" alt="image" src="https://github.com/user-attachments/assets/197e98ba-9a91-4ef9-b517-5f08de48cfab" />

<img width="966" height="476" alt="image" src="https://github.com/user-attachments/assets/4d526f71-cb0c-4097-8d0d-9bc562df9132" />

<img width="968" height="524" alt="image" src="https://github.com/user-attachments/assets/1bf00bdd-c3f5-43c3-a12b-0a7f8e35fabe" />



