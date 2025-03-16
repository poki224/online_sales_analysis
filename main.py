
from product import Product;
from product_manager import ProductManager

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