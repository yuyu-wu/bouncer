age = input('Enter your age: ')

if age:
    if int(age) >= 18 and int(age) < 21:
        print('You can enter, but need a wristband!')
    elif int(age) >= 21:
        print('You are good to enter and can drink!')
    else:
        print('You can\'t come in, little one!')
else: 
    print('Please enter a valid age: ')