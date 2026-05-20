'''
Probelm: Even/Odd Analyzer

1. Takes a number from the user
2. Checks whether the number is:
Even
Odd

3. Also checks:

if the number is positive
negative
or zero

'''

number = int(input("Enter a number: "))


if number > 0:

    if number % 2 == 0:
        print(number, "is Even")
            
    else:
        print(number, "is Odd") 

    print(number, "is Postive")

elif number < 0:
    if number % 2 == 0:
        print(number, "is Even")
            
    else:
        print(number, "is Odd") 

    print(number, "is Negative")

elif number == 0:
    if number % 2 == 0:
        print(number, "is Even")
            
    else:
        print(number, "is Odd") 

    print(number, "is Zero")

