start = int(input('Введите число start: '))
end = int(input('Введите число end: '))
list = []
for i in range(start, end + 1):
    if i % 2 == 0:
        list.append(i)
if len(list) == 0:
    print('В этом диапазоне нет чётных чисел')
else:
    print(list)