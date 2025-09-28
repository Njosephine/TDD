#facade pattern

class Waiter:
    def take_order(self):
        print("your order has been taken")


class Chef:
     def cook_order(self):
        print("your order is being prepared")

class DeliveryBoy:
     def deliver_order(self):
        print("your order is being delivered")

## using facade pattern to hide all these complexities
class ResturantFacade:
    #what it does
    def order_food(self):
        # create three instances
        waiter = Waiter()
        chef = Chef()
        deliveryboy = DeliveryBoy()
        
        #Call the subsystem functions
        waiter.take_order()
        chef.cook_order()
        deliveryboy.deliver_order()
    
app = ResturantFacade()
app.order_food()

