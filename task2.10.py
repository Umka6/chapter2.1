def season(a):
    if (a == 1) or (a == 2) or (a == 12):
        print("это зима")
    elif (a == 3) or (a == 4) or (a == 5):
        print("это весна")
    elif (a == 6) or (a == 7) or (a == 8):
        print("это лето")
    elif (a == 9) or (a == 10) or (a == 11):
        print("это осень")
    else:
        print("Такого месяца нет")
a = int(input())
season(a)
