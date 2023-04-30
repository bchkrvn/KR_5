# APP GAME 'BATTLE'

## Описание:
В данном проекте был реализована игра SKYWARS, в которой пользователю предстоит 
сразиться с компьютером в схватке.

## Используемые технологии:
* Python
* Flask
* Docker

## Как воспользоваться:
*Первый способ:*
1) Сделать копию данного репозитория:  
`git clone ...`
2) Выполнить команду:  
`docker-compose up -d`   

*Второй способ:*
1) Сделать копию данного репозитория:  
`git clone ...`

2) Для того, чтобы запустить сервер, необходимо создать виртуально окружение на локальной машине:  
`python -m venv venv`

3) После этого активировать виртуальное окружение:  
`. venv\Scripts\activate.bat`

4) Настроить переменную окружения в файле .env:  
`FLASK_ENV='production'`

5) Запустить файл app.py:  
`flask run -h 0.0.0.0 -p 80`


Игра запущена на сервере: http://158.160.20.75