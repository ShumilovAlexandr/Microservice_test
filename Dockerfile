# Образ создается на основе python версии 3.7
FROM python:3.7-slim

# Команда для создания директории внутри контейнера
RUN mkdir /app

# Скопировал в директорию файл с зависимостями
COPY requirements.txt /app

# Выполняю установку зависимостей внутри контейнера
RUN pip3 install -r /app/requirements.txt --no-cache-dir

# Копирую содержимое microservice_test в рабочую директорию
COPY / /app

# Собственно сделал app рабочей директорией
WORKDIR /app

# Устанавливаем порт
EXPOSE 5000