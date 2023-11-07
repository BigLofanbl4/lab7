#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    lst = [float(input("Enter elemnt of list: ")) for i in range(10)]
    c = float(input("Enter C: "))

    # 1 задача: количество элементов списка, больших С;
    count = 0
    for elem in lst:
        if elem > c:
            count += 1
    print(f"Count of elements greater than {c}: {count}")

    # 2 задача: произведение элементов списка, расположенных после максимального по модулю элемента.
    maxElemIndex = lst.index(max(lst))
    product = 1
    for elem in lst[maxElemIndex + 1 :]:
        product *= elem
    print(f"Product: {product}")

    # Преобразование списка
    lst.sort(key=lambda x: x >= 0)
    print(lst)
