# services/order_service.py
from models.order import Order

class OrderEngine:
    def __init__(self, inventory):
        self.inventory = inventory
        self.orders = {}
        self.next_id = 1

    def place_order(self, user, cart):
        total = sum(qty * 100 for qty in cart.items.values())

        order = Order(user, cart.items, total)
        order.id = self.next_id

        self.orders[self.next_id] = order
        self.next_id += 1

        cart.items.clear()
        return order