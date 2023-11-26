#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    string_1 = input("Введите первую строку: ")
    string_2 = input("Введите вторую строку: ")

    set_1 = set(string_1)
    set_2 = set(string_2)

    common_characters = set_1.intersection(set_2)
    common_characters = ', '.join(sorted(common_characters))  # Для красивого вывода, отсортируем и объединим символы

    print(f"Общие символы в обеих строках: {common_characters}")
