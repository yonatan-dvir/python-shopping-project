from store import Store

POSSIBLE_ACTIONS = [
    'search_by_name',
    'search_by_hashtag',
    'add_item',
    'remove_item',
    'checkout',
    'exit'
]

ITEMS_FILE = 'items.yml'


def read_input():
    line = input('What would you like to do?')
    args = line.split(' ')
    return args[0], ' '.join(args[1:])

def display_search_results(results):
    print('Search results:')
    for item in results:
        print(f"- {item.name}")

def display_shopping_cart(cart):
    print('Current shopping cart:')
    for item in cart:
        print(f"- {item.name}")

def main():
    store = Store(ITEMS_FILE)
    action, params = read_input()

    while action != 'exit':
        if action not in POSSIBLE_ACTIONS:
            print('No such action...')
            continue

        if action == 'checkout':
            print(f'The total of the purchase is {store.checkout()}.')
            print('Thank you for shopping with us!')
            return

        if action == 'search_by_name' or action == 'search_by_hashtag':
            results = getattr(store, action)(params)
            display_search_results(results)
        else:
            try:
                getattr(store, action)(params)
            except Exception as e:
                print(f"Error: {e}")

        display_shopping_cart(store._shopping_cart.cart_items)
        action, params = read_input()





if __name__ == '__main__':
    main()
