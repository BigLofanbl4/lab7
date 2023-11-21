#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = [i for i in a if i % 11 == 0 and i > 0]

    diff = b[0]
    for num in b[1:]:
        diff -= num

    print(f"Differnce {diff}")
    print(f"Count: {len(b)}")
