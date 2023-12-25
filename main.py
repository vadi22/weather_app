from fastapi import FastAPI
from utils import weather_by_city

app = FastAPI()
city_name = 'Novosibirsk'


@app.get('/weather/')
def read_item():
    temperature = weather_by_city(city_name)
    return {'city': city_name, 'temp': temperature}
