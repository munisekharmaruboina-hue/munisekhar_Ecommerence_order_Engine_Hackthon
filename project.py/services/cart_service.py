from models.cart import Cart

class CartService:
    def __init__(self):
        self.carts = {}

    def get_cart(self, user):
        if user not in self.carts:
            self.carts[user] = Cart()
        return self.carts[user]