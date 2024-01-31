import yaml
from item import Item
from shopping_cart import ShoppingCart

class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items

    # Returns a sorted list of all the items that match the search name (or contain it)
    def search_by_name(self, item_name: str) -> list:
        matching_names = [cart_item for cart_item in self._items if cart_item.name.__contains__(item_name)]
        return matching_names

    # Returns a sorted list of all the items matching the searches hashtag
    def search_by_hashtag(self, hashtag: str) -> list:
        matching_hashtags = [cart_item for cart_item in self._items if cart_item.hashtags.__contains__(hashtag)]
        return matching_hashtags

    def add_item(self, item_name: str):
        # TODO: Complete
        pass

    def remove_item(self, item_name: str):
        # TODO: Complete
        pass

    def checkout(self) -> int:
        # TODO: Complete
        pass

    def print_cart(self):
        for item in self._items:
            print(item.name)