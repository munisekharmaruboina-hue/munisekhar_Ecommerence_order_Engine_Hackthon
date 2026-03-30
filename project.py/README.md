# E-Commerce Backend Simulation

## 1. Project Overview
This is a **Python-based e-commerce backend simulation** that demonstrates the core functionalities of an online shopping system. The project includes inventory management, shopping cart operations, order placement, payment processing, discount application, fraud detection, and audit logging. It is designed to be **modular, thread-safe, and extensible** for demonstration or learning purposes.

---

## 2. Features Implemented
1. **Inventory Management**
   - Add, view, and track products
   - Stock reservation and low-stock alerts
   - Thread-safe stock operations

2. **Cart Management**
   - Add, update, and remove items
   - Reserve stock when items are added
   - View cart contents

3. **Order Management**
   - Place orders from cart
   - Order states: Created, Paid, Shipped, Delivered, Cancelled, Failed
   - Apply discounts via discount rules
   - Idempotency check to prevent duplicate orders

4. **Payment Handling**
   - Simulated payment with success/failure
   - Retry mechanism
   - Rollback stock on payment failure

5. **Discount Engine**
   - Percentage-based and coupon-based discounts
   - Rules:
     - Total > 1000 → 10% off
     - Quantity > 3 of the same product → 5% off
     - Coupons: `SAVE10` (10% off), `FLAT200` (₹200 off)

6. **Fraud Detection**
   - Alerts for multiple orders in a short time
   - Alerts for high-value orders

7. **Audit Logging**
   - Logs actions like order placement, payment, and stock changes
   - Timestamped logs for monitoring

---

## 3. Design Approach
- **Object-Oriented Design**: Classes for Product, Cart, Order, Inventory, and Services.  
- **Modular Structure**: Separate folders for models, services, systems, and utilities.  
- **Concurrency Handling**: Thread locks used for stock reservations.  
- **Idempotency Support**: Prevents duplicate order submissions.  
- **Extensible**: Easy to add new features like coupons, shipping, or real payment gateways.  

**Modules Breakdown:**
- `models/` → Data classes like Product, Order  
- `services/` → Core services (Inventory, Cart, OrderEngine, Payment, Discount)  
- `systems/` → Support systems (AuditLogger, FraudDetection, ReservationSystem)  
- `utils/` → Helpers like IdempotencyManager  
- `main.py` → Demonstrates the full workflow  

---

## 4. Assumptions
1. Product price is **simulated as 100 per quantity unit**.  
2. Payment success is randomized for demonstration purposes.  
3. Stock is **reserved immediately** when items are added to cart.  
4. Discount rules are applied **after order creation**.  
5. Idempotency tokens are used to prevent duplicate order placement.  
6. The system runs in a **single Python environment**, not connected to a real database.  

---

## 5. How to Run the Project

1. **Clone the repository**:

```bash
git clone https://github.com/munisekharmaruboina-hue/munisekhar_Ecommerence_order_Engine_Hackthon.git
cd project.py
2. Create and activate a virtual environment (optional but recommended):
 # Create virtual environment
python -m venv .venv

# Activate environment
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
3. Run the main script:
python main.py
