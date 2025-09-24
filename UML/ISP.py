## Interface Segregation Principle

#abc helps in creating abstractions
from abc import ABC, abstractmethod
#Interface for Marrying
class Marriage(ABC):
    @abstractmethod
    def getMarried(self):
        pass

#Interface for preaching
class  Preacher(ABC):
    @abstractmethod
    def preach(self):
        pass

##Imam implementing both Marriage and Preach

class Imam(Marriage, Preacher):
    def getMarried(self):
        print("Imam gets married")

    def preach(self):
        print("Imam is preaching")

#Monk implements only Preacher interface

class Monk(Preacher):
    def  preach(self):
        print("Monk is preaching")

#Calling /Usage/Testing
 
monk = Monk()
monk.preach()
    
imam = Imam()
imam.preach()
imam.getMarried()

    
         
     