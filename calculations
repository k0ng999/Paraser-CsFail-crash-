import csv

file_input = input('''Какой файл вам нужен
Введите 0 если data.csv
Введите 1 если day1.csv
Введите 2 если day2.csv
Введите 3 если day3.csv
Введите 4 если day4.csv
Введите 5 если day5.csv
Введите 6 если day6.csv
Введите 7 если day7.csv
Введите 8 если day8.csv
Введите 9 если day9.csv
Введите 10 если day10.csv
Введите 11 если day11.csv
''')

print("\n" * 100)

file_add = None
if file_input == '0':
    file_add = 'data.csv'
elif file_input == '1':
    file_add = 'day1.csv'
elif file_input == '2':
    file_add = 'day2.csv'
elif file_input == '3':
    file_add = 'day3.csv'
elif file_input == '4':
    file_add = 'day4.csv'
elif file_input == '5':
    file_add = 'day5.csv'
elif file_input == '6':
    file_add = 'day6.csv'
elif file_input == '7':
    file_add = 'day7.csv'
elif file_input == '8':
    file_add = 'day8.csv'
elif file_input == '9':
    file_add = 'day9.csv'
elif file_input == '10':
    file_add = 'day10.csv'
elif file_input == '11':
    file_add = 'day11.csv'
elif file_input == '12':
    file_add = 'day12.csv'

with open(file_add, 'r', newline='', encoding='UTF-8') as file:
    count_greater_than_10 = 0
    count_less_than_10 = 0

    range_greater_than_10 = 0
    range_lees_then_10 = 0

    q_1 = 0
    q_2 = 0

    range_greater_than_5 = 0
    range_lees_then_5 = 0

    reader = csv.reader(file)
    header = next(reader)
    calculate = []

    for row in reader:
        calculate.append(int(row[0]))
    print(f'Сумма всех ставок: {sum(calculate)}')
    for num in calculate:
        if num > 10:
            count_greater_than_10 += 1
        elif num < 10:
            count_less_than_10 += 1

    print(
        f"Чисел больше 10: {count_greater_than_10} - {count_greater_than_10 * 100 / (count_less_than_10 + count_greater_than_10):.2f}%")
    print(
        f"Чисел меньше 10: {count_less_than_10} - {count_less_than_10 * 100 / (count_less_than_10 + count_greater_than_10):.2f}%")

    for i in calculate:
        if i > 10:
            range_greater_than_10 += 1.0
        elif i < 10:
            range_lees_then_10 += float((10 - i) / 10)
    print(f'Заработал ${range_lees_then_10:.2f}, Потерял ${range_greater_than_10:.2f}')

    for i in calculate:
        if i < 10:
            if i >= 6:
                q_1 += 1
            elif i <= 5:
                q_2 += 1
    print(f'больше 5: {q_1}, меньше 5: {q_2}')

    for i in calculate:
        if i > 5:
            range_greater_than_5 += 0.5
        elif i <= 5:
            range_lees_then_5 += float((10 - i) / 10)
    print(f'Заработал ${range_lees_then_5:.2f}, Потерял ${range_greater_than_5:.2f}')

    balance = 10
    for bet in calculate:
        if balance:
            if bet > 5:
                balance -= 0.5
            elif bet < 5:
                balance += float((10 - bet) / 10)
    print(f'{balance:.2f}  =  {balance - 8:.2f}')
    colum = 0
    colum1 = 0
    sumcolum = 10
    for i in calculate:
        if i >= 40:
            if i <= 50:
                sumcolum = sumcolum + (50-i)/10
                colum += 1
                print(sumcolum)
            if i >= 51:
                sumcolum = sumcolum - 1
                print(sumcolum)
                colum1 += 1
    print(colum)
    print(colum1)
