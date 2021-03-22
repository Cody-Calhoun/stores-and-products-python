class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        

    def add_product(self, new_product):
        self.products.append(new_product)
        print(self.products[len(self.products)-1])
        # print(self.products)
    
    def print_info(self):
        print(self.products[len(self.products)-1].name)

    def sell_product(self, id):
        self.products.pop(id)
        return self

    def __str__(self):  
        return self.print_info() 
        # [
        # {name: shirt, category:clothing, price:123},
        
        # ]

        # print(self.products[0]["name"])

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        percentage = percent_change / 100
        if is_increased == True:
            self.price *= (1 + percentage) 
        else: 
            self.price *= (1 - percentage) 
        return self.price

    def print_info(self):
        # info = f"Name: {self.name}, Category: {self.category}, Price: ${self.price}"
        print(self)
        
    # def __repr__(self):
    #     return f"<PRODUCT: Name: {self.name}>"

    def __str__(self):  
        return f"Name: {self.name}, Category: {self.category}, Price: ${self.price}" 
            
        
shirt = Product("shirt", 123, "clothing")
pants = Product("pants", 123, "clothing")


# print(shirt.update_price(25, True))
# shirt.print_info()
# print(shirt.update_price(7, False))
Nordstrom = Store("Nordstrom")
Nordstrom.add_product(shirt)
Nordstrom.add_product(pants)
# Nordstrom.sell_product(1)
# Nordstrom.print_info()