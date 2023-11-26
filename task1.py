#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    user_input = input("Введите строку: ").lower()  # Получаем строку от пользователя и приводим к нижнему регистру
    vowel_count = sum(1 for char in user_input if char in vowels)  # Подсчитываем количество гласных
    result = vowel_count

    print(f"Количество гласных букв в строке: {result}")
