def num(x,y,z):
    if x>y>z:
        print(x)
    elif y>x>x:
        print(y)
    else:
        print(z)
x = int(input('Введите число:'))
y = int(input('Введите число:'))
z = int(input('Введите число:'))
num(x,y,z)