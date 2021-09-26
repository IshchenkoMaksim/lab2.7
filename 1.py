#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    glas = set("aeiouyаеёиоуыэюя")

    while True:
        word = list(input("Введите слово: "))
        x = 0
        for i in word:
            if i in glas:
                x += 1

        print(x)
