# lets implement recursion function using factorial
# it is implement using stack , stack uses Last in first Out

def factorial(num):
    if num == 1:
        return num 
    else:
        return num * factorial(num-1)

## lets test our function
print(factorial(5))