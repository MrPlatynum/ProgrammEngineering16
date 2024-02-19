#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from replace_chars_module import replace_repeated_chars

if __name__ == "__main__":
    replace_char = input('Введите символ, на который необходимо заменить повторяющиеся символы: ')
    replace_func = replace_repeated_chars(replace_char)

    input_string = input('Введите строку: ')

    result = replace_func(input_string)
    print(result)
