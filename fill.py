import requests
import settings
import constants

if __name__ == '__main__':
    requests.delete('http://127.0.0.1:5000/products')
    print(requests.post('http://127.0.0.1:5000/products', json=constants.products).content)

    requests.delete('http://127.0.0.1:5000/categories')
    for category in constants.categories.values():
        print(requests.post('http://127.0.0.1:5000/categories', json=category).content)
