print('Доступные единицы: мм, см, км, м, mi, yd')
input_1 = input('Из какой единицы: ').lower()
input_2 = input('В какую единицу: ').lower()
value = float(input('Введите значение: '))

to_meters = {
    'мм': 0.001,
    'см': 0.01,
    'м': 1,
    'км': 1000,
    'mi': 1609.344,
    'yd': 0.9144
}

if input_1 in to_meters and input_2 in to_meters:
    answer = value * to_meters[input_1] / to_meters[input_2]
    print(f'{value} {input_1} = {answer} {input_2}')
else:
    print('Введены неизвестные единицы измерения')