Маленький API-сервис для учёта инцидентов

#### 1. Создать пользователя и базу данных в PostgreSQL:
CREATE ROLE "user" WITH LOGIN NOINHERIT CREATEDB PASSWORD 'user';
CREATE DATABASE itracker WITH OWNER = "user" ENCODING = 'UTF8';