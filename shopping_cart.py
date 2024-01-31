from errors import ItemAlreadyExistsError, ItemNotExistError
from item import Item


class ShoppingCart:
    # Construct a shopping_cart by init a list to store items in the shopping cart
    def __init__(self):
            self.cart_items = []

    def add_item(self, item: Item):
        # Check if an item with the same name already exists
        for cart_item in self.items:
            # If yes, raise an ItemAlreadyExistsError
            if cart_item.name == item.name:
                raise ItemAlreadyExistsError(f"Item '{item.name}' already exists in the shopping cart.")

        # If not, add the item to the shopping cart
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        # Check if an item with the same name already exists
        for cart_item in self.items:
            # If yes, remove it from the shopping cart list
            if cart_item.name == item_name:
                self.cart_items.remove(cart_item)
                break;

        # If not, raise an ItemNotExistError
        raise ItemNotExistError(f"Item '{item_name}' does not exist in the shopping cart.")

    def get_subtotal(self) -> int:
        # TODO: Complete
        pass
