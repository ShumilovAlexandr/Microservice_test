# Образ создается на основе python версии 3.7
FROM python:3.7-slim

# Указываю рабочую директорию
WORKDIR /app

# Скопировал в директорию файл с зависимостями
COPY requirements.txt /app

# Копирую содержимое microservice_test в рабочую директорию
COPY ./ /app

# Выполняю установку зависимостей внутри контейнера
RUN pip3 install -r requirements.txt --no-cache-dir

# Устанавливаем порт
EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]


# Надо придумать как запустить приложение flask, что-то не запускается
#CMD ["flask", "run", "app.py"]




#CMD ["python", "app/app.py"] #образ и контейнер собираются, но приложение не работает при тестировании