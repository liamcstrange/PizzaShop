# TODO Claim this as your own work by modifying the following...
# File: pizza_shop.py 
# Author: Liam Strange
# Id: 45603
# Description: Pizza Shop
# This is my own work as defined by the Academic Integrity policy. 
import math





# TODO Write your classes here...

class Food:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_name(self):
        self.__name = name

    def set_price(self):
        self.__price = price

    def equals(self, other):
        if type(self) == type(other):
            if self.__name == other.__name:
                if self.__price == other.__price:
                    return True
        return False

    def clone(self):
        return Ingredient(self.__name, self.__price)


class PizzaBase(Food):

    def __init__(self, diameter):
        self.__diameter = diameter
        self.__cost = cost

    def get_diameter(self):
        return self.__diameter

    def set_diameter(self):
        self.__diameter = diameter

    def get_cost(self):
        return self.__cost

    def set_cost(self):
        self.__cost = cost

    def cal_cost_square_inch(self):
        radius = self.__diameter / 2
        area = math.pi * radius ** 2
        cost_per_square_inch = cost / area

    def set_pizza_diameter_price(self):
        sizes = {"small": 10, "medium": 12, "large": 14}
        if size in sizes:
            self.set_diameter(sizes[size])
        else:
            raise ValueError("Invaild size. Choose small, medium or large")
    
    def equals(self, other):
        if type(self) == type(other):
            if self.__diameter == other.__diameter:
                if self.__cost == other.__cost:
                    return True
        return False


    def clone(self):
        return PizzaBase(self.__diameter)
    




def main():
    # TODO Write your main program code here...
    print("~~ Welcome to the Pizza Shop ~~")
    print()



# WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()