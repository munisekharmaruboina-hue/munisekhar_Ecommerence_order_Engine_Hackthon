class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, pid, qty, inventory):
        if pid not in inventory.products:
            print("Product not found!")
            return
        product = inventory.products[pid]

        if qty > product.stock:
            print("Not enough stock!")
            return

        self.items[pid] = self.items.get(pid, 0) + qty
        product.stock -= qty

    def remove_item(self, pid, inventory):
        if pid in self.items:
            qty = self.items.pop(pid)
            inventory.products[pid].stock += qty

    def view_cart(self):
        print(self.items)