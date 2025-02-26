# Установка

### 1. Клонируйте репозиторий:

Для начала клонируйте репозиторий на свой локальный компьютер:

bash git clone https://github.com/MaksimSamusik/WeatherChecker.git

### 2. Перейдите в каталог проекта:

cd WeatherChecker

### 3. Создайте и активируйте виртуальное окружение:

python3 -m venv .venv

### 4. Установите зависимости:

pip install -r requirements.txt

### 5. Создайте файл .env в корне проекта и добавьте следующие строки:

POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db_name
POSTGRES_HOST=db
POSTGRES_PORT=5432
WEATHER_API_KEY=your_weather_api_key

Замените your_username, your_password, your_db_name на актуальные значения для вашей базы данных.
WEATHER_API_KEY — это ключ для доступа к API погоды. Получите его, зарегистрировавшись на OpenWeather.

### 6. Настройка Docker ( По желанию):
Если вы хотите развернуть приложение с использованием Docker, используйте следующие шаги:

1) Создайте Docker образ для вашего приложения:

docker build -t weatherchecker .

2)Запустите контейнер:

docker run -d -p 8000:8000 --name weatherchecker weatherchecker

3) Используйте docker-compose для работы с многоконтейнерными приложениями, если требуется.

# Использование

1) Запустите приложения:

uvicorn main:app --reload

2) Введите в адрессную строку вашего браузера
 http://127.0.0.1:8000/main

3) Введите в поле ввода город и нажмите кнопку "Посмотреть погоду"
Вам выведится информация о погоде в выбранном городе, а также история ваших запросов


# Примечания:
Приложение использует PostgreSQL для хранения информации о запросах и пользователях.
Перед использованием проверьте, что база данных настроена корректно и что все зависимости установлены.
