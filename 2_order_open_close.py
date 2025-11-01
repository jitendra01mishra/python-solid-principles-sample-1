# in this example, the payment processing classes implement the Open/Closed Principle
# by allowing new payment methods to be added without modifying existing code.
# however it if paypal payment processing needed a different way to verify security or 
# instead of a security code needed an email,
# passing email in security code will not be a good design. 

from abc import ABC, abstractmethod

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

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: ${security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: ${security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing PayPal payment type")
        print(f"Verifying email address : ${security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("Mouse", 1, 25)
order.add_item("Monitor", 2, 200)

print(f"Total price: ${order.total_price()}")

print("\n---\n")

dprocessor = DebitPaymentProcessor()
dprocessor.pay(order, "1234")

print("\n---\n")

cprocessor = CreditPaymentProcessor()
cprocessor.pay(order, "6789")

print("\n---\n")

pprocessor = PaypalPaymentProcessor()
pprocessor.pay(order, "test@test.com")