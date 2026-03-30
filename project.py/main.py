from services.inventory_service import Inventory
from services.cart_service import CartService
from services.order_service import OrderEngine
from services.payment_service import PaymentGateway
from services.discount_service import DiscountEngine
from systems.fraud_detection import FraudDetectionSystem
from systems.audit_logger import AuditLogger
from utils.idempotency import IdempotencyManager

def main():
    # --- Setup ---
    print("Initializing system...")
    inventory = Inventory()
    cart_service = CartService()
    order_engine = OrderEngine(inventory)
    payment_gateway = PaymentGateway()
    discount_engine = DiscountEngine()
    fraud_system = FraudDetectionSystem()
    audit_logger = AuditLogger()
    idempotency_mgr = IdempotencyManager()

    # --- Add Products ---
    inventory.add_product(1, "Laptop", 10)
    inventory.add_product(2, "Phone", 5)
    inventory.add_product(3, "Headphones", 20)
    print("\nCurrent Inventory:")
    for p in inventory.products.values():
        print(p)

    # --- User Adds to Cart ---
    user = "user1"
    cart = cart_service.get_cart(user)
    cart.add_item(1, 2, inventory)  # 2 Laptops
    cart.add_item(3, 5, inventory)  # 5 Headphones
    print(f"\n{user}'s Cart:")
    cart.view_cart()

    # --- Place Order ---
    token = "order_token_123"  # for idempotency
    if not idempotency_mgr.is_duplicate(token):
        order = order_engine.place_order(user, cart)
        if order:
            print("\nOrder Placed:")
            print(order)

            # --- Apply Discounts ---
            discount_engine.apply_discounts(order)
            print("\nAfter Discounts:")
            print(order)

            # --- Process Payment ---
            if payment_gateway.process_payment(order):
                order.status = "Paid"
                print(f"\nPayment completed for Order[{order.id}]")
            else:
                print(f"\nPayment failed for Order[{order.id}]")

            # --- Fraud Check ---
            fraud_system.check(user, order)

            # --- Audit Log ---
            audit_logger.log(f"Order {order.id} processed for {user}")
    else:
        print("Duplicate order prevented by idempotency check.")

    # --- View Remaining Inventory ---
    print("\nRemaining Inventory:")
    for p in inventory.products.values():
        print(p)


if __name__ == "__main__":
    main()