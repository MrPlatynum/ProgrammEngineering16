#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def replace_repeated_chars(replace_char):
    def inner_function(input_string):
        result = ''
        prev_char = ''

        for char in input_string:
            if char != prev_char:
                result += char
                prev_char = char
            else:
                result += replace_char

        return result

    return inner_function
