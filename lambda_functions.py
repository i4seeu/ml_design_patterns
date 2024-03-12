# Basic lambda function definition
# Define a lambda function that adds two numbers
add = lambda x, y: x + y

# Call the lambda function
result = add(3, 5)
print(result)  # Output: 8

# Sort a list of tuples based on the second element of each tuple
pairs = [(6, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

## a function to sort using the first element in tuple now
pairs.sort(key=lambda pair: pair[0])
print(pairs)

# Use lambda function with filter() to filter out even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]