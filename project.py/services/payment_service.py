import random

class PaymentGateway:
    def process_payment(self, order):
        if random.choice([True, False]):
            print("Payment success")
            order.status = "Paid"
            return True
        print("Payment failed")
        return False