x = int(input('Podaj liczbe:'))
y = int(input('Podaj potege do ktorej chcesz podniesc ta liczbe :'))

def potegi(x, y) -> int:
    if x or y ==0:
        raise Exception('liczby nie moge byc 0')
    return x ** y
print(potegi(x, y))

x1 = int(input('Podaj liczbe:'))
y1 = int(input('Podaj potege do ktorej chcesz podniesc ta liczbe :'))

def dodawanie(x,y):
    return x + y
print(dodawanie(x1,y1))





