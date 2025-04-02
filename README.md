# WeatherChecker

WeatherChecker is an application for checking the weather, providing the user with up-to-date weather information for a given city.

## Installation

### 1. Clone the repository:

To begin, clone the repository to your local machine:

```bash
git clone https://github.com/MaksimSamusik/WeatherChecker.git
```

### 2. Navigate to the project directory:

```bash
cd WeatherChecker
```

### 3. Create and activate a virtual environment:

python3 -m venv .venv

Activate the virtual environment:

On Linux/MacOS:
```bash
source .venv/bin/activate
```


On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies:
Install the required dependencies for the project:

```bash
pip install -r requirements.txt
```

### 5. Create a .env file in the root of the project and add the following lines:

```bash
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db_name
POSTGRES_HOST=db
POSTGRES_PORT=5432
WEATHER_API_KEY=your_weather_api_key
```

Replace your_username, your_password, your_db_name with the actual values for your database.
WEATHER_API_KEY is the key for accessing the weather API. Obtain it by registering on OpenWeather.

### 6. Docker setup (Optional):
If you want to deploy the app using Docker, follow these steps:

Create a Docker image for your app:

```bash
docker build -t weatherchecker
```

Run the container:

```bash
docker run -d -p 8000:8000 --name weatherchecker weatherchecker
```

Use docker-compose for working with multi-container applications if needed.

## Usage

### 1. Run the application:
To run the app, use the following command:

```bash
uvicorn main:app --reload
```

### 2. Enter the following URL in your browser:

```bash
http://127.0.0.1:8000/main
```

### 3. Enter the city name in the input field and click the "Check Weather" button. The weather information for the selected city, along with the history of your queries, will be displayed.

## Notes:
The application uses PostgreSQL to store information about queries and users.
Before use, make sure that the database is set up correctly and all dependencies are installed.
