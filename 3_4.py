class Wallet:

    def __init__(self, currency: str, name: str, payment_system: str, balance: float):
        self.balance = balance
        self.currency = currency
        self.name = name
        self.payment_system = payment_system

    def info(self):
        print(f"Текущий счет: {self.balance} {self.currency}")

    def get_money(self):
        print('Пополнение баланса:')
        add = float(input("Сумма пополнения: "))
        self.balance += add
        print('Успешное пополнение счета')
    
    def spend_money(self):
        print('Оплата')
        throw = float(input("Сумма платежа: "))
        if throw < self.balance:
            self.balance -= throw
            print('Успешная оплата')
        else:
            print('Недостаточно средств для оплаты')

    def delete_accaunt(self):
            del self.balance
            del self.currency
            del self.name
            del self.payment_system
            print('Счет удален')
            exit()

def wallet_menu():
    print("""
          1. Пополнение баланса
          2. Оплата
          3. Проверить баланс
          4. Удаление счета

          Выберите операцию
          """)
    while True:
        try:
            act = int(input())
            break
        except ValueError:
            print("Неправильный ввод.Введите целое число")

    if act == 1:
        w.get_money()
    elif act == 2:
        w.spend_money()
    elif act == 3:
        w.info()
    elif act == 4:
        w.delete_accaunt()
        
    print("Вернуться в меню (д/н)")
    r = input()
    if r == 'д':
        wallet_menu()
    elif r == 'н':
        exit()
    else:
        print('ValueError')
        exit()

name = (input('Введите название кошелька: '))

while True:  
    cur = (input('Выберите валюту (USD, EUR, RUB, BYN): '))
    if cur in ("USD", "EUR", "RUB", "BYN"):
        break
    else:
        print("Введена неверная валюта")

while True:
    ps = (input('Выберите платежную систему (МИР, Qiwi, Visa, MasterCard): '))
    if ps in ("МИР", "Visa", "MasterCard", "Qiwi"):
        break
    else:
        print("Введена неверная платёжная система")

w = Wallet(cur, name, ps, balance = 0)

print(f""" 
        Кошелек {w.name}
        Используемая платежная система: {w.payment_system}
          """)

wallet_menu()


    