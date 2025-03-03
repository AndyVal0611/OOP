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
        return f'Electronics: {self.name}, Price: ₱{self.price}, Year of Warranty: {self.warranty_period}'


# Subclass Clothing
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return f'Clothing: {self.name}, Price: ₱{self.price}, Size: {self.size}'


# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f'Added to cart: {product.name}')

    def view_cart(self):
        if not self.cart:
            print('\nYour cart is empty.')
        else:
            print('\nShopping Cart:')
            for index, product in enumerate(self.cart, start=1):
                print(f'{index}. {product.get_info()}')

    def checkout(self):
        if not self.cart:
            print('\nYour cart is empty. Add items before checking out.')
        else:
            total_price = sum(product.price for product in self.cart)
            print(f'\nTotal Price: ₱{total_price}')
            print('Checkout complete. Thank you for shopping!')


# Initialize Product objects
electronics1 = Electronics("Lenovo ThinkPad Laptop", 50000, 2)
electronics2 = Electronics("iPhone 16", 54000, 1)
electronics3 = Electronics("Huawei MatePad T10", 35500, 1)
clothing1 = Clothing("H&M Flare Jeans (Dark Blue)", 900, "S")
clothing2 = Clothing("Levi's Denim Jacket", 1800, "L")
clothing3 = Clothing("Guess Woven Faux Suede Trench Coat", 2800, "XL")

products = [electronics1, electronics2, electronics3, clothing1, clothing2, clothing3]


# Display all products instantly
print("\nWELCOME TO AV DEPARTMENT STORE!"
      "\n...a store of everyone's essentials")
print('\nAvailable Products:')
for idx, product in enumerate(products, start=1):
    print(f'{idx}. {product.get_info()}')


# Get user choice for adding products
def select_products(cart):
    try:
        selections = input('Enter product numbers to add (comma-separated): ')
        selected_indexes = [int(i) - 1 for i in selections.split(',')]
        for index in selected_indexes:
            if 0 <= index < len(products):
                cart.add_to_cart(products[index])
            else:
                print(f'Invalid selection: {index + 1}')
    except ValueError:
        print('Invalid input. Please enter numbers separated by commas.')


# Main loop for user interaction
def start_shopping():
    cart = ShoppingCart()

    while True:
        print('\nMenu:')
        print('1. Add products to cart')
        print('2. View cart')
        print('3. Checkout')
        print('4. Exit')

        try:
            choice = int(input('Enter your choice (1-4): '))
            if choice == 1:
                select_products(cart)
            elif choice == 2:
                cart.view_cart()
            elif choice == 3:
                cart.view_cart()
                cart.checkout()
            elif choice == 4:
                print('Thank you for shopping! Have a great day!')
                break
            else:
                print('Invalid choice. Please select a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter a number.')

start_shopping()