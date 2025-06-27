from src.category import Category


def test_category(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Mobile Phones"
    assert first_category.description == "cool"
    assert len(first_category.products) == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2
