def factorial(x):
    if x == 0:
        return 1
    return factorial(x-1) *x
x = int(input('enter the number'))
print(factorial(x))

