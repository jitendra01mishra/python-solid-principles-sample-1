# in this example, the payment processing classes implement the :
# 
# single responsibility principle, 
# open/closed principle, 
# liskov substitution principle,
# Interface segregation - voliation 
# 
# by replacing the objects of the parent class with objects of the subclass classes instance 
# without affecting the correctness of the program,
# however, if we have include the auth method here we need modfiy all the subclasses to 
# implement the auth method which violates the open/close principal and 
# also payment processor is now having more responsibility which is a voliation of single responsibility.

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

class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass

class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code):
        super().__init__()
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Authenticating debit payment type: {code}")
        self.verified = True
        print("SMS code verified")

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        
        print("Processing debit payment type")
        print(f"Verifying security code: ${self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        super().__init__()
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: ${self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, email_address):
        super().__init__()
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Authenticating debit payment type: {code}")
        self.verified = True
        print("SMS code verified")

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        
        print("Processing PayPal payment type")
        print(f"Verifying security code: ${self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("Mouse", 1, 25)
order.add_item("Monitor", 2, 200)

print(f"Total price: ${order.total_price()}")

print("\n---\n")

dprocessor = DebitPaymentProcessor("1234")
dprocessor.auth_sms(2345)
dprocessor.pay(order)

print("\n---\n")

cprocessor = CreditPaymentProcessor("56789")
cprocessor.pay(order)

print("\n---\n")

pprocessor = PaypalPaymentProcessor("test@test.com")
pprocessor.auth_sms(6789)
pprocessor.pay(order)
