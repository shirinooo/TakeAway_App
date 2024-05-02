from lib.dish import Dish

class DishList:

    def __init__(self):
        self.dish_list = {}

    def add_dish(self, dish):
        dish.dish_is_available()
        if dish.available_dish():
            self.dish_list[dish.dish_name] = dish.dish_price

    def get_dish_list(self):
        return self.dish_list

