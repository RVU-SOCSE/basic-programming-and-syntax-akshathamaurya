#program to find factorial
#akshatha r
#1RUA25BCA0009

def fact(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact(a - 1)

num = int(input("Enter a number: "))

print("Factorial of", num, "is", fact(num))
