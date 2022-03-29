import csv
# Four key princimples of oop
# Encapsulation: restricting the direct access of some attributes in a program
# Abstraction: hiding unecesarry information from the instances, eg by using private methods
# Inheritance: code reuse across classes
# Polymophisim: use of a single type entity for multiple objects
# Abstract classes are similar to interfaces in other languages

class Item:
    pay_rate = 0.8
    cart = []


    def __repr__(self) -> str:
        return self.name

    def __init__(self, name: str, price: int, quantity=0) -> None:
        # dynamic attibute assignment
        assert price >= 0, f"Price {price} is not >= 0"
        assert quantity >=0
        self.__name = name#__ make it a private attribute that can't be accessed out of the class
        self.price = price
        self.quantity = quantity
        Item.cart.append(self)

    # restricting users to change certain attributes
    # readonly attibutes once set in the constructor
    # encapsulation
    #works like a getter
    @property
    def name(self):
        return self.__name

    #name setter
    @name.setter
    def name(self, name):
        self.__name = name

    #private method, will only be assesed inside the class
    def __connect(self):
        pass


    def calculate_total_price(self) -> int:
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate#good advise to assess class attributes from the instance level to allow instance level attributes with the same name

    @classmethod#usually used to instantiate objects
    def instantiate_from_csv(cls):

        f = open("items.csv")
        reader = csv.reader(f)
        for name, price, quantity in reader:
            Item(name, int(price), int(quantity))

    @staticmethod#used when doing something that has a relationship with the class but not unique per instance
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    


item2 = Item("kfkf", 100,7)
item2.name = "Jengo"
print(item2.name)


# item1 = Item("kfkf", 100,7)
# print(dir(item1))
# print(Item.calculate_total_price(item1))
# print(item1.__dict__)#instance level attributes
# print(Item.__dict__)#class level attibutes
# print(item1.apply_discount())
# item2 = Item("kfkf", 100,7)
# item2.pay_rate = 0.7
# print(item2.apply_discount())
# print(Item.instantiate_from_csv())
# print(Item.cart)
# print(Item.is_integer(7.9))



class Phone(Item):
    
    def __init__(self, name: str, price: int, broken_phones = 0, quantity=0) -> None:
        super().__init__(name, price, quantity=quantity)
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not >= 0"
        self.broken_phones = broken_phones 


phone1 = Phone("techno", 500, 9)
print(isinstance(phone1, Item))