import threading
from models.product import Product

class Inventory:
    def __init__(self):
        self.products = {}
        self.lock = threading.Lock()

    def add_product(self, pid, name, stock):
        if pid in self.products:
            print("Duplicate product!")
            return
        self.products[pid] = Product(pid, name, stock)

    def low_stock_alert(self, threshold=2):
        for p in self.products.values():
            if p.stock <= threshold:
                print("Low stock:", p)