# Program to find maximum and minimum without using split()
#akshatha r
#usn-1RUA25BCA0009
n = int(input("How many numbers do you want to enter? "))


if n <= 0:
    print("Invalid count.")
else:
    
    num = int(input("Enter number 1: "))
    max_val = num
    min_val = num

    
    for i in range(2, n + 1):
        num = int(input(f"Enter number {i}: "))

        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num


    print("Maximum value:", max_val)
    print("Minimum value:", min_val)
