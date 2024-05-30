from praktikum.database import Database


class TestDatabase:
    def test_database_initialization(self):
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
