def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

number = int(input("Enter a number: "))
print(f"Factroial of {number} is: {fact(number)}")


import math
def func(n):
    sq_root = math.sqrt(n)
    logarithm = math.log(n)
    Sine = math.sin(n)
    print(f"Square root: {sq_root}")
    print(f"Logarithm: {logarithm}")
    print(f"Sine: {Sine}")    

number = int(input("Enter a number: "))
func(number)
