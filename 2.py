#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    while True:
        word1 = set(input("Введите 1-oe слово: "))
        word2 = set(input("Введите 2-oe слово: "))
        repeat = word1.intersection(word2)

        if repeat == set():
            print("Нет одинаковых букв")
        else:
            print("Повторяющиеся буквы: ", repeat)
