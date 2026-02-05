#program to find leap year
#akshatha r
#usn-1RUA25BCA0009

year =int (input("enter a value:"))
if year%4==0 or year%100==0:
    print (year ,"leap year")
else:
    print ("no leap year")
