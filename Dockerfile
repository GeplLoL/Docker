FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Сбор статических файлов (если нужно)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Запускаем встроенный сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
