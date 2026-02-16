import json


def save_file_to_json(grocery_stock: dict[str, int]) -> None:
    # save back to json file
    with open("grocery_stock.json", "w", encoding="utf-8") as file:
        json.dump(grocery_stock, file, indent=2, ensure_ascii=False)


class Product:
    def __init__(self, product_name: str, stock: int = 0):
        self.name: str = product_name
        self.stock: int = stock
        self.purchases: list[dict[str, int | str]] = []

    def add_product(self, product_quantity: int) -> None:
        if product_quantity <= 0:
            raise ValueError("Amount must be bigger than 0")

        self.stock += product_quantity

    def buy_product(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self.stock:
            raise ValueError("There are not enough items in stock")

        # reduce stock
        self.stock -= quantity

        # record purchase
        self.purchases.append({
            "product_name": self.name,
            "quantity": quantity
        })


class ShoppingCart:
    def __init__(self):
        # { product_name: quantity }
        self.items: dict[str, int] = {}

    def add_item(self, shop: "Shop", product_name: str, quantity: int) -> None:
        product_name = product_name.strip()

        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not shop.has_product(product_name):
            raise ValueError(f"{product_name} not available in shop")
        if product_name in self.items:
            self.items[product_name] += quantity
        else:
            self.items[product_name] = quantity

    def remove_item(self, product_name: str, quantity: int) -> None:
        product_name = product_name.strip()

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if product_name not in self.items:
            raise ValueError("Product not in your shopping cart")

        if quantity > self.items[product_name]:
            raise ValueError("Not enough quantity in cart")

        self.items[product_name] -= quantity

        if self.items[product_name] == 0:
            del self.items[product_name]

    def view_basket(self) -> None:
        if not self.items:
            print("Shopping cart is empty")
            return

        for product, quantity in self.items.items():
            print(f"{product}: {quantity}")

    def clear_basket(self) -> None:
        self.items.clear()


class Shop:
    def __init__(self):
        # products stored as: {product_name: Product}
        self.products: dict[str, Product] = {}

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if product.name in self.products:
            self.products[product.name].stock += quantity
        else:
            product.stock = quantity
            self.products[product.name] = product

    def list_products(self) -> None:
        if not self.products:
            print("No products available")
            return

        for name, product in self.products.items():
            print(f"{name}: {product.stock} available")

    def has_product(self, product_name: str) -> bool:
        return product_name.strip() in self.products

    def get_product(self, product_name: str) -> Product:
        product_name = product_name.strip()
        if product_name not in self.products:
            raise ValueError("Product not found")
        return self.products[product_name]

    def reduce_stock(self, product_name: str, quantity: int) -> None:
        product_name = product_name.strip()

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        product = self.get_product(product_name)
        if quantity > product.stock:
            raise ValueError("Not enough stock available")

        product.stock -= quantity

    def pay(self, shopping_cart: ShoppingCart) -> None:
        if not shopping_cart.items:
            raise ValueError("Shopping cart is empty")

        # check everything first
        for product_name, quantity in shopping_cart.items.items():
            if product_name not in self.products:
                raise ValueError(f"{product_name} not available in shop")

            if quantity > self.products[product_name].stock:
                raise ValueError(f"Not enough stock for {product_name}")

        # reduce stock
        for product_name, quantity in shopping_cart.items.items():
            self.products[product_name].stock -= quantity

        # convert products → dict for json
        grocery_stock: dict[str, int] = {
            name: product.stock
            for name, product in self.products.items()
        }

        save_file_to_json(grocery_stock)

        # clear cart after purchase
        shopping_cart.clear_basket()
        print("Payment successful")


def main() -> None:
    # Create shop
    shop = Shop()

    # Load JSON file
    try:
        with open("grocery_stock.json", "r", encoding="utf-8") as file:
            grocery_stock: dict[str, int] = json.load(file)
    except FileNotFoundError:
        grocery_stock = {}

    # Fill shop from JSON
    for name, qty in grocery_stock.items():
        product = Product(name, stock=qty)
        shop.add_product(product, qty)

    cart = ShoppingCart()

    while True:
        print("\n--- Blabla Shop ---")
        print("1) Add product to shop")
        print("2) View available items in shop")
        print("3) Add item to shopping cart")
        print("4) remove item from shopping cart")
        print("5) clear shopping cart")
        print("6) view basket")
        print("7) Pay")
        print("0) Exit")

        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                product_name = input("Product you would like to add: ").strip()
                quantity = int(input("What is the quantity you want to stock up the store with this product? ").strip())
                product = Product(product_name, stock=quantity)
                shop.add_product(product, quantity)
                print(f"Product added to stock")

            elif choice == "2":
                shop.list_products()

            elif choice == "3":
                product_name = input("Product you would like to add to the cart: ").strip()
                quantity = int(input("How many items would you like to add? ").strip())
                cart.add_item(shop, product_name, quantity)

            elif choice == "4":
                product_name = input("Product you would like to remove from the cart: ").strip()
                quantity = int(input("How many items would you like to remove? ").strip())
                cart.remove_item(product_name, quantity)

            elif choice == "5":
                cart.clear_basket()

            elif choice == "6":
                cart.view_basket()

            elif choice == "7":
                shop.pay(cart)

            elif choice == "0":
                exit()

            else:
                raise ValueError("Please type in a number between 0 and 8")

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()