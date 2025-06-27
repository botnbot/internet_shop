import json
import os
from typing import Any


from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    fullpath = os.path.abspath(path)
    with open(fullpath, "r", encoding="Utf-8") as file_obj:
        data = json.load(file_obj)
        return data


def create_objects(data: dict) -> list[Category]:
    categories = []
    for item in data:
        products = [Product(**prod) for prod in item["products"]]
        category = Category(name=item["name"], description=item["description"], products=products)
        categories.append(category)
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    product_data = create_objects(raw_data)
    for i in range(len(product_data)):
         print(product_data[i].products)

    print(f'Всего {Category.product_count} продукта-(ов) в {Category.category_count} категориях')
