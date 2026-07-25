import requests

def extract_product_data():
    try:
        url = "https://dummyjson.com/products"
        res = requests.get(url, timeout=10)
        data = res.json()
        return data
    except requests.exceptions.HTTPError as err:
        print("HTTP error: ", err.args[0])