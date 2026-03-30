class Order:
    def __init__(self, user, items, total):
        self.user = user
        self.items = items.copy()
        self.total = total
        self.status = "Created"
        self.id = None

    def __str__(self):
        return f"Order[{self.id}] {self.status} - {self.items} - ₹{self.total}"