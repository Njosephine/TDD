from abc import ABC , abstractmethod

class InputDevice(ABC):
    @abstractmethod
    def input(self):
        pass

class ProcessingDevice(ABC):
    @abstractmethod
    def process(self):
        pass

class OutputDevice(ABC):
    @abstractmethod
    def output(self):
        pass

class StorageDevice(ABC):
    @abstractmethod
    def storage(self):
        pass

#Implentation
class Keyboard(InputDevice):
    def input(self):
        print("Tying using a keyboard")


class Mouse(InputDevice):
    def input(self):
        print("Typing using a mouse")

class CPU(ProcessingDevice):
    def input(self):
       print("CPU process the data")

class Printer(OutputDevice):
    def output(self):
       print("CPU process the data")


class Monitor(StorageDevice):
    def input(self):
       print("CPU process the data")
