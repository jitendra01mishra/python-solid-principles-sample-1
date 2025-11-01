# in this example, the Order class has only order responsibilities and 
# pyament processing is handled by separate classes.
# This code is okay Single Responsibility Principle. 
# however it still violates the Open/Closed Principle because
# every time a new payment method is added, the PaymentProcessor class must be modified. 

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"


    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)


    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: ${security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: ${security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("Mouse", 1, 25)
order.add_item("Monitor", 2, 200)

print(f"Total price: ${order.total_price()}")

print("\n---\n")

processor = PaymentProcessor()
processor.pay_debit(order, "12345")

print("\n---\n")

processor = PaymentProcessor()
processor.pay_credit(order, "12345")
