class Product:
    def __init__(self, pid, name, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        self.id = pid
        self.name = name
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Stock: {self.stock}"