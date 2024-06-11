import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredientCreation:

    @pytest.mark.parametrize("ingredient_type", [
        (INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING)
    ])
    def test_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Test Ingredient", 10.0)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", [
        ("Hot Sauce"),
        ("Patty"),
        ("Ketchup")
    ])
    def test_ingredient_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 10.0)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [
        (10.0),
        (20.0),
        (5.0)
    ])
    def test_ingredient_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Test Ingredient", price)
        assert ingredient.get_price() == price
