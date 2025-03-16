from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Added {product.name} to cart.")

    def calculate_total(self):
        return sum(product.price for product in self.cart_items)

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("Cart contents:")
            for product in self.cart_items:
                print(f"- {product.name}: ${product.price}")
            print(f"Total amount: ${self.calculate_total()}")
