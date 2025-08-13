from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditPaymentStrategy(PaymentStrategy):
    
    def pay(self, amount):
        print(f"Paying amount {amount} using credit")

class DebitPaymentStrategy(PaymentStrategy):
    
    def pay(self, amount):
        print(f"Paying amount {amount} using debit")

class UPIPaymentStrategy(PaymentStrategy):
    
    def pay(self, amount):
        print(f"Paying amount {amount} using UPI")

class Payment:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        self.strategy.pay(amount)

class PaymentStrategyFactory:
    def get_strategy(self, method):
        mapping = {
            "credit":CreditPaymentStrategy(),
            "debit":DebitPaymentStrategy(),
            "upi":UPIPaymentStrategy()
        }
        return mapping[method]


payment_strategy_factory = PaymentStrategyFactory()

# credit_strategy = CreditPaymentStrategy()
# debit_strategy = DebitPaymentStrategy()
# upi_strategy = UPIPaymentStrategy()

payment = Payment(payment_strategy_factory.get_strategy('credit'))
payment.checkout(100)
payment.set_strategy(payment_strategy_factory.get_strategy('debit'))
payment.checkout(200)
payment.set_strategy(payment_strategy_factory.get_strategy('upi'))
payment.checkout(300)


# 1️⃣ Why did you use the Strategy Pattern here instead of simple if/else statements?
# Good answer:
# The Strategy Pattern decouples the payment process from the payment method logic.
# This means:
# We can add new payment methods without modifying the Payment class.
# We avoid duplicated if/else logic across multiple parts of the system.
# We can swap strategies at runtime — useful for fallback flows (e.g., if card fails, try UPI automatically).

# 2️⃣ How would you handle runtime selection of strategy based on config or user choice?
# Good answer:
# Right now, we manually pass strategies to the Payment object.
# In production, we’d integrate a Factory Pattern that maps a string (e.g., "credit") to the correct strategy instance.
# Example:
# class PaymentStrategyFactory:
#     def get_strategy(self, method: str) -> PaymentStrategy:
#         mapping = {
#             "credit": CreditPaymentStrategy(),
#             "debit": DebitPaymentStrategy(),
#             "upi": UPIPaymentStrategy()
#         }
#         return mapping[method]
# This allows dynamic selection based on a database config, API request, or feature flag.