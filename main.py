
from product import Product;
from product_manager import ProductManager
from cart import Cart
import random

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Racunar", 300, 2))
manager.add_product(Product("Tastatura", 50, 50))
manager.add_product(Product("gejmerski mis", 120, 15))
manager.add_product(Product("Gejmerski laptop", 1500, 20))

# Kreiranje instance klase Cart
cart = Cart()

# Dodavanje tri slučajno odabrana proizvoda u korpu
selected_products = random.sample(manager.products, 3)
for product in selected_products:
    cart.add_to_cart(product)

# Prikaz sadržaja korpe i ukupne vrednosti
cart.display_cart()