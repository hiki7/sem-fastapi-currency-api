from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = 'fca_live_CmWuQPIlV4d3wHOl3uFPzYlKVUVdDQfIJVYoSjF0'
BASE_URL = 'https://api.freecurrencyapi.com/v1/latest'


@app.get("/currency")
def get_currency(base_cur: str, conv_cur: str):
    response = requests.get(f"{BASE_URL}?apikey={API_KEY}&base_cur={base_cur}&conv_cur={conv_cur}")

    data = response.json()

    if response.status_code != 200:
        return {"error": "Not found"}

    return {
        "base_currency": base_cur,
        "converted_currency": conv_cur,
        "value": data['data'][conv_cur]
    }


