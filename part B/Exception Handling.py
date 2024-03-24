try:
    a = int(input('Enter a'))
    b = int(input('Enter b'))
    c = a / b
    print('a/b is =', c)
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print("I am in else block")
finally:
    print('I always execute')
