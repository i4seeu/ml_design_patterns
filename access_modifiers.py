class MyClass:
    def __init__(self):
        self.public_attribute = "I'm public"
        self.__private_attribute = "I'm private"
        self._protected_attribute = "I'm protected"

    def get_private_attribute(self):
        return self.__private_attribute

# Creating an instance of MyClass
obj = MyClass()

# Accessing public attribute
print(obj.public_attribute)  # Output: I'm public

# Accessing private attribute (Name Mangling)
# This is discouraged and should be avoided
print(obj._MyClass__private_attribute)  # Output: I'm private

# Accessing protected attribute (Convention)
# This is also discouraged but not prevented
print(obj._protected_attribute)  # Output: I'm protected

# Accessing private attribute using getter method
print(obj.get_private_attribute())  # Output: I'm private
