
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added.")

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total inventory value: {total_value}")
