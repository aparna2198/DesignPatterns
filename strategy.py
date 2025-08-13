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


credit_strategy = CreditPaymentStrategy()
debit_strategy = DebitPaymentStrategy()
upi_strategy = UPIPaymentStrategy()

payment = Payment(credit_strategy)
payment.checkout(100)
payment.set_strategy(debit_strategy)
payment.checkout(200)
payment.set_strategy(upi_strategy)
payment.checkout(300)
