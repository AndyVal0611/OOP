from abc import ABC, abstractmethod


# Abstract class Product
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self):
        pass


# Subclass Electronics
class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def get_info(self):
        return f'{self.name} (₱{self.price}) - Warranty: {self.warranty_period} years'


# Subclass Clothing
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return f'{self.name} (₱{self.price}) - Size: {self.size}'


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart(self):
        print('\nShopping Cart:')
        for index, product in enumerate(self.cart, start=1):
            print(f'{index}. {product.get_info()}')

    def checkout(self):
        total_price = sum(product.price for product in self.cart)
        print(f'Total Price: ₱{total_price}')


# User interaction
def main():
    cart = ShoppingCart()

    print('Enter details for two electronics items:')
    for _ in range(2):
        name = input('Enter product name: ')
        price = int(input('Enter price: '))
        warranty = int(input('Enter warranty period (years): '))
        cart.add_to_cart(Electronics(name, price, warranty))

    print('\nEnter details for two clothing items:')
    for _ in range(2):
        name = input('Enter product name: ')
        price = int(input('Enter price: '))
        size = input('Enter size: ')
        cart.add_to_cart(Clothing(name, price, size))

    # View cart and checkout
    cart.view_cart()
    cart.checkout()


if __name__ == '__main__':
    main()
