import json
import os
from typing import Any

from src.product import Product


def read_json(path: str) -> Any:
    fullpath = os.path.abspath(path)
    with open(fullpath, 'r', encoding='Utf-8') as file_obj:
        data = json.load(file_obj)
        return data

def create_objects(data: json) -> Any:
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
    return categories

if __name__ == '__main__':
    print()