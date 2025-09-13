n1 = input('Введите первое целое число: ')
n2 = input('Введите второе целое число: ')
n3 = input('Введите третье целое число: ')
if n1 < n2 and n1 < n3:
    print(n1)
if n2 < n1 and n2 < n3:
    print(n2)
if n3 < n1 and n3 < n2:
    print(n3)