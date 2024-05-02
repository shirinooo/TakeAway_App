class Dish:

    def __init__(self, dish_name, dish_price):

        if dish_name == "" or dish_price == 0:
            raise Exception("Dish Name and Dish Price must be filled")
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.is_avalable = False

    def dish_is_available(self):
        self.is_avalable = True

    def available_dish(self):
        return self.is_avalable

        
