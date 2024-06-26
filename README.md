# Kittygram Project
[![Main Kittygram Workflow](https://github.com/posk43/kittygram_final/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/posk43/kittygram_final/actions/workflows/main.yml)
## Описание

Kittygram - это веб-приложение для обмена фотографиями котиков. Taski - это другой проект, связанный с задачами.

## Стек технологий

- Python 3.9.16
- Node.js v18.17.1
- Backend: Django
- Frontend: React
- Nginx
- Gunicorn

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ваш_логин/kittygram
   cd kittygram

repo_owner: ваш_логин_на_гитхабе
kittygram_domain: полная ссылка (https://доменное_имя) на ваш проект Kittygram
taski_domain: полная ссылка (https://доменное_имя) на ваш проект Taski
dockerhub_username: ваш_логин_на_докерхабе


Скопируйте содержимое файла `.github/workflows/main.yml` в файл `kittygram_workflow.yml` в корневой директории проекта.

Для локального запуска тестов создайте виртуальное окружение, установите в него зависимости из backend/requirements.txt и запустите в корневой директории проекта `pytest`.

## Чек-лист для проверки перед отправкой задания

- Проект Taski доступен по доменному имени, указанному в `tests.yml`.
- Проект Kittygram доступен по доменному имени, указанному в `tests.yml`.
- Пуш в ветку main запускает тестирование и деплой Kittygram, а после успешного деплоя вам приходит сообщение в телеграм.
- В корне проекта есть файл `kittygram_workflow.yml`.

## Что нужно сделать 
 
Настроить запуск проекта Kittygram в контейнерах и CI/CD с помощью GitHub Actions 
 
## Как проверить работу с помощью автотестов 
 
В корне репозитория создайте файл tests.yml со следующим содержимым: 
yaml 
repo_owner: ваш_логин_на_гитхабе 
kittygram_domain: полная ссылка (https://доменное_имя) на ваш проект Kittygram 
taski_domain: полная ссылка (https://доменное_имя) на ваш проект Taski 
dockerhub_username: ваш_логин_на_докерхабе 

 
Скопируйте содержимое файла `.github/workflows/main.yml` в файл `kittygram_workflow.yml` в корневой директории проекта. 
 
Для локального запуска тестов создайте виртуальное окружение, установите в него зависимости из backend/requirements.txt и запустите в корневой директории проекта `pytest`. 
 
## Чек-лист для проверки перед отправкой задания 
 
- Проект Taski доступен по доменному имени, указанному в `tests.yml`. 
- Проект Kittygram доступен по доменному имени, указанному в `tests.yml`. 
- Пуш в ветку main запускает тестирование и деплой Kittygram, а после успешного деплоя вам приходит сообщение в телеграм. 
- В корне проекта есть файл `kittygram_workflow.yml`.
- Переменные окружения

## В .env файле укажите следующие переменные окружения:
- DEBUG - режим отладки (True/False)
- POSTGRES_USER - Имя пользователя для подключения к базе данных PostgreSQL. Это обычно учетная запись, которая будет использоваться для взаимодействия с базой данных.
- POSTGRES_PASSWORD - Пароль пользователя для подключения к базе данных PostgreSQL. Это секретная строка, необходимая для обеспечения безопасности подключения к базе данных.
- POSTGRES_DB - Название базы данных PostgreSQL, к которой будет подключено приложение. Это определяет базу данных, с которой будет работать приложение.
- DB_HOST - : Хост (адрес) базы данных PostgreSQL, к которой будет осуществлено подключение. Это может быть IP-адрес или доменное имя сервера базы данных.
- DB_PORT - Порт, на котором прослушивает сервер базы данных PostgreSQL. По умолчанию PostgreSQL использует порт 5432.
- SECRET_KEY -  Секретный ключ Django, используемый для шифрования данных, таких как сессии и пароли. Это важный параметр для обеспечения безопасности Django-приложения.
- ALLOWED_HOSTS - Список доменных имен или IP-адресов, которые приложение Django считает доверенными. Это мера безопасности, чтобы предотвратить атаки типа "Host header poisoning".

## Автор
- Лиджиев Петр (https://github.com/posk43)