def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

n = int(input("Enter a number: "))
even_or_odd(n)

def sum_till_50(n=50):
    i = 1
    sumx = 0
    while i <= n:
        sumx += i
        i += 1
    return sumx

final = sum_till_50()
print(f"The sum of numbers from 1 to 50 is: {final}")
