"""
Задание №1
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""
PROCENT_CEHS = 0.015
SUMM_WITHDRAWAL = 50
MIN_SUMM_PROCENT = 30
MAX_SUMM_PROCENT = 600
PROCENT_OPERACION = 0.03
POCENT_WEALTH = 0.1
EXCEEDING_THE_AMOUNNT = 5_000_000
BALANS = 0.0


def amount_of_money() -> float:
    while True:
        result = float(input("Введите сумму: "))
        if result % SUMM_WITHDRAWAL == 0:
            return result
        else:
            print("Сумма должна быть кратной 50 у.е.")


def wealth_test():
    global BALANS
    if BALANS > EXCEEDING_THE_AMOUNNT:
        BALANS -= (BALANS * PROCENT_OPERACION) / 100


def exercise_1():
    print()
    print("Задание №1")
    FLAG = True
    COUNT = 0
    global BALANS
    while FLAG:
        print(
            f"Меню (Выберите действие.)\n1. Пополнить\n2. Снять\n3. Баланс \n4. Выйти"
        )
        num = input("Введите номер из меню: ")
        if num.isnumeric() and 1 <= int(num) <= 4:
            if num == "1":
                BALANS += amount_of_money()

            elif num == "2":
                withdraw_money = amount_of_money()
                if MIN_SUMM_PROCENT >= withdraw_money <= MAX_SUMM_PROCENT:
                    withdraw_money_procent = withdraw_money + (
                        (withdraw_money * 0.015) / 100
                    )
                    if BALANS >= withdraw_money_procent:
                        BALANS -= withdraw_money_procent
                        wealth_test()
                        COUNT += 1
                    else:
                        print("У Вас не хватает денег")
                elif COUNT == 3:
                    if BALANS > 0:
                        BALANS += (BALANS * PROCENT_OPERACION) / 100
                else:
                    if BALANS >= withdraw_money:
                        BALANS -= withdraw_money
                        wealth_test()
                        COUNT += 1
                    else:
                        print("У Вас не хватает денег")

            elif num == "3":
                print(f"Баланс = {BALANS}")

            elif num == "4":
                print("Вы закончили операции")
                FLAG = False
        else:
            print("Вы ошиблись. Повторите ещё раз. ")


"""
Задание №2
✔ Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
"""


def get_hex(num: int) -> str:
    hex_digits = "0123456789abcdef"
    result = ""
    while num > 0:
        result = hex_digits[num % 16] + result
        num = num // 16
    return f"0x{result}"


def exercise_2():
    while True:
        number = input("Ввдите число: ")
        if number.isnumeric():
            number = int(number)
            print()
            print("Задание №2")
            print(f"Вычисление  = {get_hex(number)}")
            print(f'Проверка через "%#x" = {"%#x" % number}')
            print(f"Проверка через hex = {hex(number)}\n")
            break


"""
Задание №3
✔ Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions.

"""
import fractions
import re


def separation_of_signs(f: str):
    num, denom = map(int, f.split("/"))
    return num, denom


def examination_summa(
    num_1: int, denom_1: int, num_2: int, denom_2: int, sign: str
) -> str:
    frac_1 = fractions.Fraction(num_1, denom_1)
    frac_2 = fractions.Fraction(num_2, denom_2)
    if sign == "+":
        result = frac_1 + frac_2
    elif sign == "*":
        result = frac_1 * frac_2
    return result


def Calculating_the_amount(num_1: int, denom_1: int, num_2: int, denom_2: int) -> str:
    if denom_1 == denom_2:
        if num_1 + num_2 == denom_1:
            result = "1"
        else:
            result = f"{num_1 + num_2}/{denom_1}"

    else:
        sum_frac_num = num_1 * denom_2 + num_2 * denom_1
        sum_frac_denom = denom_1 * denom_2

        if sum_frac_num == sum_frac_denom:
            result = "1"
        else:
            result = f"{sum_frac_num}/{sum_frac_denom}"
    return result


def calculate_product(num_1: int, denom_1: int, num_2: int, denom_2: int) -> str:
    sum_frac_num = num_1 * num_2
    sum_frac_denom = denom_1 * denom_2
    return f"{sum_frac_num}/{sum_frac_denom}"


def proverka_re(num: str) -> bool:
    if re.search(r"\d/\d", num):
        result = True
    else:
        result = False
    return result


def exercise_3():
    count = 1
    print()
    print("Задание №3")
    while True:
        if count == 1:
            fraction_1 = input(f"Введите {count} значение типа a/b: ")
            if proverka_re(fraction_1):
                count += 1
            else:
                print("Вы ошиблись. Повторите ещё раз.")
                print()
        elif count == 2:
            fraction_2 = input(f"Введите {count} значение типа a/b: ")
            if proverka_re(fraction_2):
                break
            else:
                print("Вы ошиблись. Повторите ещё раз.")
                print()
    numerator_1, denominator_1 = separation_of_signs(fraction_1)
    numerator_2, denominator_2 = separation_of_signs(fraction_2)

    print(
        f"Сумма дробей {fraction_1} + {fraction_2} = {Calculating_the_amount(numerator_1, denominator_1, numerator_2, denominator_2)}"
    )
    print(
        f"Проверка: {fraction_1} + {fraction_2} = {examination_summa(numerator_1, denominator_1, numerator_2, denominator_2, '+')}"
    )
    print(
        f"Произведение дробей {fraction_1} * {fraction_2} = {calculate_product(numerator_1, denominator_1, numerator_2, denominator_2)}"
    )
    print(
        f"Проверка: {fraction_1} * {fraction_2} = {examination_summa(numerator_1, denominator_1, numerator_2, denominator_2, '*')}\n"
    )


if __name__ == "__main__":
    while True:
        print(
            f"Меню (Выберите действие.)\n1. Задание 1\n2. Задание 2\n3. Задание 3\n4. Выход"
        )
        num = input("Введите номер из меню: ")
        if num.isnumeric() and 1 <= int(num) <= 4:
            match num:
                case "1":
                    exercise_1()
                case "2":
                    exercise_2()
                case "3":
                    exercise_3()
                case "4":
                    break
        else:
            print("Вы ошиблись. Повторите ещё раз. ")
