#program foe
def fib(n):
    a = 0
    b = 1

    print(a)
    print(b)

    i = 2
    while i < n:
        c = a + b
        print(c)
        a = b
        b = c
        i += 1

# Read number of terms
n = int(input("Enter number of terms: "))

fib(n)
