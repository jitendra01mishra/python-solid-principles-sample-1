# in the previous example the approach was still not ideal as the
# PaymentProcessor_SMS interface forced all payment processors to implement the auth_sms method
# In this version, we separate the SMS authentication functionality into its own class, SMSAuth.
# which more composition over inheritance. this make it more flexible and adheres to the interface segregation principle.
# However it still has some dependency issues that will be addressed in the next example. please refer below issues satement.

# in the previous example the class depended on a SMSAuth if we also have to add not a robot authentication it will become messy
# In this version, we apply the dependency inversion principle by depending on abstractions rather than concrete implementations.


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


class SMSAuth:


    def __init__(self):
        self._verified = False


    def verify_code(self, code):
        print(f"Authenticating via SMS code: {code}")
        self._verified = True


    @property
    def is_authenticated(self):
        return self._verified


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):


    def __init__(self, security_code, authorizer: SMSAuth):
        super().__init__()
        self.security_code = security_code
        self.authorizer = authorizer


    def pay(self, order):
        if not self.authorizer.is_authenticated:
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


class PaypalPaymentProcessor(PaymentProcessor):


    def __init__(self, email_address, authorizer: SMSAuth):
        super().__init__()
        self.email_address = email_address
        self.authorizer = authorizer


    def pay(self, order):
        if not self.authorizer.is_authenticated:
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

authorizer = SMSAuth()
processor = DebitPaymentProcessor("1234", authorizer=authorizer)
authorizer.verify_code(123456)
processor.pay(order)
