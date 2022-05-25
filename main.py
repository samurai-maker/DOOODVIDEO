import requests
import os
from os import getenv

api_key = getenv("API_KEY")

url1 = f'https://doodapi.com/api/upload/server?key={api_key}'

def get_link(file_name, caption):

    h = requests.get(url1).json()
    print(h['result'])

    params = (
        (f'{api_key}', ''),
    )

    files = {
        'api_key': (None, f'{api_key}'),
        'file': (f'{caption}.mp4', open(f'{file_name}', 'rb')),
    }

    response = requests.post(f'{h["result"]}', params=params, files=files).json()
    return response