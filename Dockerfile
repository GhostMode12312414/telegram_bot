FROM python:3.9-slim

WORKDIR /app

# Копируем requirements.txt из корневой папки
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЕ файлы из корневой папки
COPY . .

# Копируем папку scripts с ботом
COPY scripts/ ./scripts/

# Запускаем бота из папки scripts
CMD ["python", "scripts/telegram_bot.py"]