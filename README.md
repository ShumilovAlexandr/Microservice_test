# Задача: разработка микросервиса на любом из предложенных фреймворков

## Требования и задачи
Используя один из framework (Flask, Django, FastApi) создать микросвервис:

## Задача сервиса
На запрос

    GET /api/meta 
вернуть список файлов и директорий с датой их создания которые находятся в указанной директории.

Пример ответа:

    {
       "data":[
            {
                "name": "src",
                "type": "folder",
                "time": 1665996554107
            },
            {
                "name": "file.py",
                "type": "file",
                "time": 1665996554108
            },
        ]
    }
Корневая директория ставится в config.py <br/>
Язык программирования: Python 3.7+ <br/>
Код должен соответствовать PEP <br/>
Использование Docker, сервис должен запускаться с помощью docker-compose up. <br/>

# Как запустить готовый проект
1. Клонировать проект по ссылке <https://github.com/ShumilovAlexandr/Microservice_test>
2. Если тестируете проект на локальном компьютере, замените в файле app/config.py на актуальный адрес
3. Если тестируете проект через Postman: <br/>
   а) Создайте образ проекта командой docker build -t <имя образа> . <br/>
   б) Далее, применив команду docker-compose up, создайте и запустите контейнер <br/>
   в) Протестируйте приложение, указан в адресной строке __http://127.0.0.1:5000/api/meta__ и применив запрос __GET__. <br/>
   
### Стек технологий
![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue)
![PyPI - Docker Version](https://img.shields.io/badge/docker-20.10.17-blue)
![PyPI - flake8 Version](https://img.shields.io/badge/flake8-4.0.1-blue)
![PyPI - Python-dotenv Version](https://img.shields.io/badge/python--dotenv-0.20.0-blue)
![PyPI - Python-dotenv Version](https://img.shields.io/badge/flask-2.2.2-blue)
 
