import time
from collections import defaultdict

class FraudDetectionSystem:
    def __init__(self):
        self.user_orders = defaultdict(list)

    def check(self, user, order):
        now = time.time()
        self.user_orders[user].append(now)

        recent = [t for t in self.user_orders[user] if now - t < 60]
        if len(recent) >= 3:
            print("Fraud Alert!")