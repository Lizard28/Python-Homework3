class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def multi(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Деление на 0 недопустимо")
        return x / y

    def pow(self, x, y):
        return x ** y

def menu():
    print("Меню калькулятора:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. ** или ^")
    print("6. ВЫХОД")

calc = Calculator()
while True:
    menu()
    choice = input("Выберите какую оперцию хотите совершить(1-6):")
    
    if choice not in {'1', '2', '3', '4', '5', '6'}:
        print("Неверный ввод, такой операции нет")
        continue

    if choice == '6':
        print("Выход из программы")
        break

    while True:
        try:
            num1= float(input("Введите первое число: "))
            break
        except ValueError:
            print("Было введено не число")

    while True:
        try:
            num2= float(input("Введите второе число: "))
            break
        except ValueError:
            print("Было введено не число")

    if choice == '1':
            result = calc.add(num1, num2)
    elif choice == '2':
            result = calc.sub(num1, num2)
    elif choice == '3':
            result = calc.multi(num1, num2)
    elif choice == '4':
        try:
            result = calc.div(num1, num2)
        except ZeroDivisionError as e:
            print(e)
            continue

    elif choice == '5':
            result = calc.pow(num1, num2)
    else:
        print("Неверный ввод. Введите число 1-6")
        
    print("Итог: ", result)

