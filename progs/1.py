#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = [int(input("Enter number: ")) for i in range(10)]
    b = []

    for num in a:
        if num % 11 == 0 and num > 0:
            b.append(num)

    diff = b[0]
    for num in b[1:]:
        diff -= num

    print(f"Differnce {diff}")
    print(f"Count: {len(b)}")
