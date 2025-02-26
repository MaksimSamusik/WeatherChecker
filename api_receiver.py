import requests


API_KEY = "API_KEY"


async def get_data(city: str):
    api_url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    )

    response = requests.get(api_url)
    data = response.json()
    return data
