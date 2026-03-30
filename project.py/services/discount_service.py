class DiscountEngine:
    def apply_discounts(self, order):
        if order.total > 1000:
            order.total *= 0.9