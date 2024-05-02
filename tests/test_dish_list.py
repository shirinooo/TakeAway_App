from lib.dish_list import DishList
from unittest.mock import Mock

def test_add_dish_if_dish_is_available_and_get_dishlist():
    mock_dish = Mock()
    dish_list = DishList() 
    mock_dish.dish_name = "Pizza"
    mock_dish.dish_price = 12.5
    mock_dish.available_dish.return_value = True
    dish_list.add_dish(mock_dish)

    assert  dish_list.get_dish_list() == {"Pizza": 12.5}