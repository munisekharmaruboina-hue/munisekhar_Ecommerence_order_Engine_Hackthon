class ReturnRefundSystem:
    def process_return(self, order, pid, qty, inventory):
        if pid not in order.items or qty <= 0:
            print("Invalid return request.")
            return
        if qty > order.items[pid]:
            print("Cannot return more than purchased.")
            return

        # Update order
        order.items[pid] -= qty
        if order.items[pid] == 0:
            del order.items[pid]

        refund_amount = qty * 100  # demo price
        order.total -= refund_amount

        # Restore stock
        inventory.products[pid].stock += qty

        print(f"Returned {qty} of product {pid}. Refund: ₹{refund_amount}. New total: ₹{order.total}")