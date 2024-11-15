# Abstract class for calculator
# Chris Brundige
# This is the abstract class for the calculator.  It takes in two numbers and performs the operation on them.

from abc import ABC, abstractmethod  # This is the import statement, it imports the ABC and abstractmethod from the abc module
from helper_functions.helper import try_except_decorator # This is the import statement, it imports the try_except_decorator module




class AbstractCalculator(
    ABC):  # This is the class definition, it defines the AbstractCalculator class and inherits from the ABC class
    @abstractmethod  # This is the decorator, it marks the add method as abstract
    def add(self, x, y):  # This is the method definition, it defines the add method
        return x + y


    @abstractmethod  # This is the decorator, it marks the subtract method as abstract
    def subtract(self, x, y):  # This is the method definition, it defines the subtract method
        pass  # This is the pass statement, it does nothing

    @abstractmethod  # This is the decorator, it marks the multiply method as abstract
    def multiply(self, x, y):  # This is the method definition, it defines the multiply method
        pass  # This is the pass statement, it does nothing

    @abstractmethod  # This is the decorator, it marks the divide method as abstract
    def divide(self, x, y):  # This is the method definition, it defines the divide method
        pass  # This is the pass statement, it does nothing

    @abstractmethod  # This is the decorator, it marks the divide method as abstract
    def power(self, x, y):  # This is the method definition, it defines the divide method
        pass  # This is the pass statement, it does nothing

    @abstractmethod  # This is the decorator, it marks the divide method as abstract
    def square_root(self, x):  # This is the method definition, it defines the divide method
        pass  # This is the pass statement, it does nothing

    @abstractmethod  # This is the decorator, it marks the divide method as abstract
    def remainder(self, x, y):
        return x % y


# class implementation

# BasicCalculator class implementation

class BasicCalculator(AbstractCalculator):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        raise NotImplementedError("This method is not implemented")

    def divide(self, x, y):
        raise NotImplementedError("This method is not implemented")

    def power(self, x, y):
        raise NotImplementedError("This method is not implemented")

    def square_root(self, x):
        raise NotImplementedError("This method is not implemented")

    def remainder(self, x, y):
        raise NotImplementedError("This method is not implemented")
# scientific_calculator.py

class ScientificCalculator(AbstractCalculator):
    @try_except_decorator
    def add(self, x, y):
        raise NotImplementedError("This method is not implemented")

    @try_except_decorator
    def subtract(self, x, y):
        raise NotImplementedError("This method is not implemented")

    @try_except_decorator
    def multiply(self, x, y):
        raise NotImplementedError("This method is not implemented")

    @try_except_decorator
    def divide(self, x, y):
        raise NotImplementedError("This method is not implemented")

    @try_except_decorator
    def power(self, x, y):
        return x ** y

    @try_except_decorator
    def square_root(self, x):
        return x ** 0.5

    @try_except_decorator
    def remainder(self, x, y):
        raise NotImplementedError("This method is not implemented")



 # This is the decorator, it marks the main function as a try_except_decorator
if __name__ == "__main__":  # This is the main function


    # Basic Calculator
    basic_calculator = BasicCalculator()

    # Use the add method

    print(basic_calculator.add(2, 3))

    # Try to use the multiply method

    print(basic_calculator.multiply(2, 3))


