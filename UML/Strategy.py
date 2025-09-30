from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using a credit card")

class MobileMoney(PaymentStrategy):
     def pay(self, amount):
        print(f"Paying {amount} using a mobile money")


# Context
class Order:
    def _init_(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


creditCard = CreditCard()
mobilemoney = MobileMoney()
order = Order() 
order.set_strategy(CreditCard())
order.process_payment(200)

order.set_strategy(MobileMoney())
order.process_payment(200)