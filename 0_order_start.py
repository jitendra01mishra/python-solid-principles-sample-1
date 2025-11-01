# in this example, the Order class has multiple responsibilities, 
# it performing the order and payment processing as well.
# This code violates the Single Responsibility Principle.

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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":    
            print("Processing debit payment type")
            print(f"Verifying security code: ${security_code}")
            status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: ${security_code}")
            status = "paid"
        else:
            raise Exception("Unknown payment type")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("Mouse", 1, 25)
order.add_item("Monitor", 2, 200)

print(f"Total price: ${order.total_price()}")

order.pay("debit", "0372846")
