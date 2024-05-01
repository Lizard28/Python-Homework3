def my_list(l: list, ch: int = 2):
    l2 = []
    for i in l:
        i = i*ch
        l2.append(i)
    return l2

while True:
    try:
        count = int(input('Число элементов списка: '))
        break
    except ValueError:
        print("Неправильное значение, ожидалось целое число")

l = []

for i in range(count):
    while True:
        el = input(f"{i+1}-е число: ")
        try:
            el_num = float(el)  
            l.append(el_num)  
            break
        except ValueError:
            print("Ошибка: введите целое или дробное число.")

my_number = input('Введите множитель или нажмите Enter(по умолчанию 2): ')
if my_number == '':
    print('Итоговый список:', my_list(l))  
else:
    my_number = int(my_number)
    print('Итоговый список:', my_list(l, my_number))