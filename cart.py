from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)
        print(f"Added '{product.name}' to the cart.")

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Cart contents:")
            for item in self.cart_items:
                print(f"- {item.name}: ${item.price:.2f} x {item.quantity}")
