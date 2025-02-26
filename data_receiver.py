import requests


city_name = input("Enter city name: ")
API_KEY = ""
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

if __name__ == '__main__':
    response = requests.get(API_URL)
    data = response.json()
    print(data)