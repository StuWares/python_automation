# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, 
# and prints Greetings! if anything else is stored in spam.
while True:
    print('Hello! Please pick 1, 2 or 3 to get a greeting')
    print('Enter 99 to exit')
    spam = int(input())
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    elif spam == 99:
        break
    else:
        print('Greetings!')