#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1. номер минимального элемента списка;
# 2. сумму элементов списка, расположенных между первым
# и вторым отрицательными элементами.
# Преобразовать список таким образом, чтобы сначала располагались
# все элементы, модуль которых не превышает 1, а потом - все остальные.

if __name__ == '__main__':
    float_list = list(map(float, input("Введите список целых чисел: ").split()))

    # Отсортируем список согласно условию задачи
    abs_list = []
    more_list = []
    for i in float_list:
        if abs(i) < 1:
            abs_list.append(i)
        else:
            more_list.append(i)
    float_list = abs_list + more_list
    print("Отсортированный список :", float_list)

    # Вычислим номер минимального элемента списка
    num_min = float_list.index(min(float_list))
    print("Номер минимального элемента списка: ", num_min+1)

    # Вычислим сумму элементов списка между
    # первыми отрицательными элементами
    first = False
    sum_num = 0
    for i in float_list:
        if i < 0:
            first = True
        if first:
            if float_list[float_list.index(i) + 1] < 0:
                first = False
                break
        if first:
            sum_num += float_list[float_list.index(i) + 1]

    print("Сумма элементов между первыми отрицательными числами: ", sum_num)
