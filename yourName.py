inputwords = 'Please type your name:'

print('Section 1:')
yourname = ''
while yourname != 'your name':
    print(inputwords)
    yourname = input()
print('Thank you!')

print('Section 2:')
while True:
    print(inputwords)
    name = input()
    if name == 'your name':
        break
print('Thank you!')

print('Section 3:')
while True:
    print('Who are you?')
    username = input()
    if username != 'Joe':
        continue
    print('Hello, Joe, what is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')