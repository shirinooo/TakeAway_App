from lib.dish import Dish
import pytest

def test_dish_constructor():
    dish = Dish("Pizza", 12.5)
    assert dish.dish_name == "Pizza"
    assert dish.dish_price == 12.5

def test_raise_error_if_dish_name_or_price_empty():
   
    with pytest.raises(Exception) as err:
        Dish("", 0)
    error_message = str(err.value)
    assert error_message == "Dish Name and Dish Price must be filled"


def test_dish_is_available():
    dish = Dish("Pizza", 12.5)
    dish.dish_is_available()
    assert dish.available_dish() == True
