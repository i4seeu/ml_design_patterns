# Create a list of squares of numbers from 1 to 5 using list comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#combining list comprehesion and decorators
def double_values(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [x * 2 for x in result]
    return wrapper

@double_values
def square_numbers(numbers):
    return [x ** 2 for x in numbers]

numbers = [1, 2, 3, 4, 5]
print(square_numbers(numbers))  # Output: [2, 4, 6, 8, 10]

