from lib.dish import Dish

def test_dish_constructor():
    dish = Dish("Pizza", 12.5)
    assert dish.dish_name == "Pizza"
    assert dish.dish_price == 12.5

def test_get_dish():
    dish_1 = Dish("Pizza", 12.5)
    assert dish_1.get_dish() == {"Pizza": 12.5} 