
from product import Product;
from product_manager import ProductManager
from cart import Cart
import random

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Monitor", 200, 12))
manager.add_product(Product("Telefon", 800, 5))
manager.add_product(Product("Tablet", 500, 7))
manager.add_product(Product("Laptop", 1200, 10))

# Prikaz svih proizvoda
manager.display_all_products()

# Prikaz ukupne vrednosti inventara
manager.total_inventory_value()

# Kreiranje instance klase Cart
cart = Cart()

# Dodavanje tri slučajno odabrana proizvoda u korpu
selected_products = random.sample(manager.products, 3)
for product in selected_products:
    cart.add_to_cart(product)

# Prikaz sadržaja korpe i ukupne vrednosti
cart.display_cart()