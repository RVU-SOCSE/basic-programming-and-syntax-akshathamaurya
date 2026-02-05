#program to find vowels and consonents
#akshatha r
#usn-1RUA25BCA0009

day = input("enter a character:")
match day:
    case 'a'|'e'|'i'|'o'|'u':
        print ("vowels")
    case _:
        print ("consonants")
