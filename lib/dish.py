class Dish:

    def __init__(self, dish_name, dish_price):
        self.dish_name = dish_name
        self.dish_price = dish_price

    def get_dish(self):
        dish = {}
        dish[self.dish_name] = self.dish_price
        return dish
