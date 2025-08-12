# stripe’s API allows merchants to create Payment Intents with many optional parameters (currency, amount, customer, metadata, payment method types, etc.).

# You need to design a PaymentIntentBuilder class in Python that:

# Implements the Builder pattern so that developers can fluently build complex payment intent objects.
# Must support the following optional properties:
# amount
# currency
# customer_id
# description
# payment_methods (list)
# metadata (dict)
# The build() method should return a dictionary representing the final payload ready to send to Stripe’s API.
# The builder should allow method chaining.


#Builder makes  creating complex objects, partially optional object safe, readable and extensible 

class PaymentIntentBuilder:
    def __init__(self):
        self.payment_methods = []
        self.amount = None
        self.currency = None
        self.metadata = None
        self.customer_id = None
        self.metadata = None
        self.description = None

    def set_amount(self, amount):
        self.amount = amount
        return self
    
    def set_currency(self, currency):
        self.currency = currency
        return self
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
        return self
    
    def set_description(self, description):
        self.description = description
        return self

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)
        return self
    
    def set_metadata(self,metadata):
        self.metadata = metadata
        return self
    
    def build(self):
        if self.amount is None or self.currency is None:
            raise ValueError('Amount and currency are required')

        return {
            "amount" : self.amount,
            "currency": self.currency,
            "metadata" :self.metadata,
            "payment_methods": self.payment_methods,
            "customer_id" : self.customer_id,
            "description":self.description
        }


payment_intent = (
    PaymentIntentBuilder()
        .set_amount(5000)
        .set_currency("usd")
        .set_customer_id("cus_12345")
        .add_payment_method("card")
        .add_payment_method("apple_pay")
        .set_metadata({"order_id": "order_9876"})
        .build()
)

print(payment_intent)



    
    
    




