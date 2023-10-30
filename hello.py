print("Hello,Python!")
print('Please input your name:')
#name = input()
#print('hi, ' + name)
#print('Never ask for help from Grey.')

a = "Hello"
print(a.split("e"))

x = int(99.99)
print(x)

name = 'Alicy'
password = 'swordfish'
age = 3000
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
elif name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, importal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')