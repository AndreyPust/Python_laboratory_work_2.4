#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо написать программу, которая из списка целых чисел составляет
# три других списка. В первый записать числа, кратные 5, во второй – числа,
# кратные 7, а в третий – оставшиеся числа (Вариант 26).

if __name__ == '__main__':
    int_list = list(map(int, input("Введите список целых чисел: ").split()))
    multiple_five = []
    multiple_seven = []
    remaining_list = []

    # Создадим из певого списка трое новых
    for i in int_list:
        if i % 5 == 0:
            multiple_five += [i]
        if i % 7 == 0:
            multiple_seven += [i]
        if i % 5 != 0:
            if i % 7 != 0:
                remaining_list += [i]

    print("Числа, кратные 5:", multiple_five)
    print("Числа, кратные 7:", multiple_seven)
    print("Оставшиеся числа:", remaining_list)
