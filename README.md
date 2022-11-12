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
3. Если тестируете проект через Postman: 
   а) Создайте образ проекта командой docker build -t <имя образа> .
   б) Далее, применив команду docker-compose up, создайте и запустите контейнер
   в) протестируйте приложение, указан в адресной строке http://127.0.0.1:5000/api/meta и применив запрос GET.
 
