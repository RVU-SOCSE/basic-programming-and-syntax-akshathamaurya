#program to find day using match case
#akshatha r
#usn-1RUA25BCA0009

day =int (input("enter a value:"))
match day:
    case 1:
        print ("monday")
    case 2 :
        print ("tuesday")
    case _:
        print ("some unknown day")
        
