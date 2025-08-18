

# The Adapter Pattern lets your code talk to external systems with different interfaces as if they were all the same — like plugging any charger into any wall with the right adapter.
class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError
        
class StripeAPI:
    def make_payment(self, money):
        print(f"Stripe paid {money}")

class RazorPayAPI:
    def do_transaction(self, money):
        print(f"Razor pay paid {money}")

class StripeAdaptor(PaymentProcessor):
    def __init__(self, stripe:StripeAPI):
        self.stripe = stripe
    
    def pay(self, amount):
        self.stripe.make_payment(amount)

class RazorAdaptor(PaymentProcessor):
    def __init__(self, razorpay:RazorPayAPI):
        self.razorpay = razorpay
    
    def pay(self, amount):
        self.razorpay.do_transaction(amount)

stripe = StripeAdaptor(StripeAPI())
razor = RazorAdaptor(RazorPayAPI())

stripe.pay(111)
razor.pay(123)




        
        