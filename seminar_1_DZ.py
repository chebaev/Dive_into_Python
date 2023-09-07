"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.

"""
a = int(input("Введите строронну а: "))
b = int(input("Введите строронну b: "))
c = int(input("Введите строронну c: "))

if a + b < c or a + c < b or b + c < a:
    print("Треугольник не существует")
else:
    print("Треугольник существует")
    if a == b != c or a == c != b or c == b != a:
        print("И являеться равнобедренный треугольник")
    elif a == b == c:
        print("И являеться равнобедренный равносторонним треугольником")
    else:
        print("И являеться равнобедренный разносторонним треугольником")

"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

"""

# MAX_NUMBER = 100000
# ERROR_TEXT = "Повторите попытку"

# def proverka(num: int):
#     result = ''
#     for elem in range(2, num):
#         if num % elem == 0:
#             result = f"Число {(num)} Состовное"
#             break
#     else:
#         result = f"Число {num} простое"

#     return result

# while True:
#     number = input("Введите число: ")
#     if number.isnumeric():
#         if 1 > int(number):
#             print(f"Вы ввели отрицательное число. {ERROR_TEXT}")
#         elif int(number) > MAX_NUMBER:
#             print(f"Вы ввели больше {MAX_NUMBER}. {ERROR_TEXT}")
#         else:
#             print(proverka(int(number)))
#             break
#     else:
#         print(f"Вы ввели не число. {ERROR_TEXT}")


"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
"""
# from random import randint
# LOWER_LIMIT = 0
# UPPER_LIMIT  = 1000
# ATTEMPT = 10
# count = 1
# randint_number = randint(LOWER_LIMIT, UPPER_LIMIT)
# print(randint_number)

# def proverka(counts:int, num:int, rand_num:int):
#     if counts == ATTEMPT and num != rand_num:
#         print('Попытки закончились. Вы не угадали.')

# while count <= ATTEMPT:
#     number = int(input(f'№{count} Введите число: '))
#     if number == randint_number:
#         print(f"Вы угадали  {randint_number}")
#         break
#     elif number > randint_number:
#         print("меньше")
#         proverka(count, number, randint_number)
#     elif number < randint_number:
#         print("больше")
#         proverka(count, number, randint_number)
#     count += 1
# if count == ATTEMPT and number != randint_number:
#     print('Попытки закончились. Вы не угадали.')
