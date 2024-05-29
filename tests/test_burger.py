from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock

def test_burger_creation():
    burger = Burger()
    assert burger.bun is None
    assert len(burger.ingredients) == 0

def test_burger_set_buns():
    burger = Burger()
    bun = Mock(spec=Bun)
    burger.set_buns(bun)
    assert burger.bun == bun

def test_burger_add_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients

def test_burger_remove_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert ingredient not in burger.ingredients

def test_burger_move_ingredient():
    burger = Burger()
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]

def test_burger_get_price():
    burger = Burger()
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 50.0
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 20.0
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == 120.0

def test_burger_get_receipt():
    burger = Burger()
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 50.0
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_price.return_value = 20.0
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert "(==== Test Bun ====)" in receipt
    assert "= filling Test Ingredient =" in receipt
    assert "Price: 120.0" in receipt
