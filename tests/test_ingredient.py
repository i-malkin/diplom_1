import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 10.0),
    (INGREDIENT_TYPE_FILLING, "Patty", 20.0),
    (INGREDIENT_TYPE_SAUCE, "Ketchup", 5.0)
])
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
