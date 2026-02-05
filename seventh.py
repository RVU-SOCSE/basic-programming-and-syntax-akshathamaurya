# program using break
# akshatha r
#usn-1RUA25BCA0009
num = int(input("Enter a number: "))

flag = 0   # 0 means prime, 1 means not prime

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")
