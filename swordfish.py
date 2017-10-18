# using break and contiune
while True: # while True creates an infinite loop
    print('Who are you?')
    name = input()
    if name != 'Joe': # this block will keep restarting the loop until Joe is entered
        continue
    print('Hello, Joe.  What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
