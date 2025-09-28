# Subsystems
class Waiter:
    def take_order(self):
        print("Waiter: Taking the order.")

class Chef:
    def cook_order(self):
        print("Chef: Cooking the order.")

class DeliveryBoy:
    def deliver_order(self):
        print("DeliveryBoy: Delivering the order.")

# Usage without Facade
waiter = Waiter()
chef = Chef()
delivery_boy = DeliveryBoy()

# The client has to call everything manually
waiter.take_order()
chef.cook_order()
delivery_boy.deliver_order()

#Complexity for the client: Every client must know all subsystems and the correct sequence to use them.
#Tight coupling: If you change how Chef or DeliveryBoy works, all client code must change.
#No single entry point: The client handles multiple steps explicitly.