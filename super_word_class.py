class ParentClass:
    def parent_method(self):
        print("Parent method")

class ChildClass(ParentClass):
    def child_method(self):
        super().parent_method()  # Calling parent method using super()
        print("Child method")

# Creating an instance of ChildClass
child_instance = ChildClass()

# Calling the child method, which will invoke the parent method using super()
child_instance.child_method()
