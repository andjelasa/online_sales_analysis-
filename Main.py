from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()

    # Add some products
    manager.add_product(Product("Laptop", 1200.0, 5))
    manager.add_product(Product("Smartphone", 800.0, 10))
    manager.add_product(Product("Headphones", 150.0, 15))

    print("All Products:")
    manager.view_products()

    total = manager.total_value()
    print(f"Total inventory value: ${total:.2f}")

if __name__ == "__main__":
    main()

# Remove a product
manager.remove_product("Smartphone")

print("\nProducts after removal:")
manager.view_products()

total = manager.total_value()
print(f"\nTotal inventory value after removal: ${total:.2f}")
