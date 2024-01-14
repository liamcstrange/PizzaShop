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


    def equals(self, other):
        if type(self) == type(other):
            if self.__name == other.__name:
                if self.__price == other.__price:
                    return True
        return False

    def clone(self):
        cloned_food = Food(self.__name, self.__price)
        return cloned_food


class PizzaBase(Food):

    def __init__(self, diameter, baseType, cost):
        self.__diameter = diameter
        self.__baseType = ["deep pan", "thin crust", "cheese crust"]
        self.__cost = cost

    def get_diameter(self):
        return self.__diameter

    def set_diameter(self):
        self.__diameter = diameter

    def calc_cost_square_inch(self):
        cost = float(self.get_price())
        diameter_size = float(self.__diameter)
        cost_per_square_inch = float((cost/3.14)) * (((diameter_size/2)**2))
        return cost_per_square_inch


    def set_pizza_diameter_price(self):
        sizes = {"small": 10, "medium": 12, "large": 14}
        if self.__diameter in sizes:
            self.set_diameter(sizes[self.__diameter])
        else:
            raise ValueError("Invaild size. Choose small, medium or large")
    
    def equals(self, other):
        if type(self) == type(other):
            if self.__diameter == other.__diameter:
                if self.calc_cost_square_inch() == other.calc_cost_square_inch():
                    if self.set_pizza_diameter_price() == other.set_pizza_diameter_price():
                        return True
        return False


    def clone(self):
        cloned_pizzabase = PizzaBase(self.__diameter, self.__baseType, self.__cost)
        return cloned_pizzabase


class Pizza(Food):
    def __init__(self, name, price, base, toppings):
        super().__init__(name, price)
        self.__original_base = base
        self.__original_toppings = toppings
        self.__current_base = base
        self.__current_toppings = toppings

    
    def get_original_base(self):
        return self.__original_base

    def get_original_toppings(self):
        return self.__original_toppings
    
    def get_current_base(self):
        return self.__current_base

    def get_current_toppings(self):
        return self.__current_toppings

    def clone(self):
        return Pizza(self.__get_name(), self.__get_price(), self.__get_current_base(), self.__get_current_toppings())

    def equals(self, other):
        if self == other and type(self):
            return True
        return False
    
    def add_topping(self, topping):
        if topping not in self.get_current_toppings():
            self.get_current_toppings().append(topping)

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)

    
    def get_price(self):
       return self.__price

class Order:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__pizza = []

    def set_pizza(self, pizza):
        self.__pizza.append(pizza)

    def get_customer_name(self):
        return self.__customer_name

    def get_pizza(self):
        return self.__pizza

    def generate_receipt(self):
        if not self.__pizzas:
            raise Exception("No pizzas so far")
        
        total_price = 0
        for pizza in self.__pizzas:
            total_price += pizza.price

        receipt = f"Total ${total_price:.2f}\n"
        receipt += f"Enjoy your meal {self.customer_name}! :)"
        return receipt

    def save_receipt(self):
        receipt = self.generate_receipt()
        with open(f"receipts/{self.customer_name}.txt", "w") as file:
            file.write(receipt)


class PizzaShop(Order):
    def __init__(self, customer_name):
        super().__init__(customer_name)

        


        

def main():
    # TODO Write your main program code here...
    print("~~ Welcome to the Pizza Shop ~~")
    print()



# WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()