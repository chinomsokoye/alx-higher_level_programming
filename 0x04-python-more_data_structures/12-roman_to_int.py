#!/usr/bin/python3
def roman_to_int(roman_string):
    val = 0
    if (roman_string and isinstance(roman_string, str)):
        r_dict = {'D': 500, 'C': 100, 'M': 1000, 'L': 50, 'X': 10, 'V': 5,
                  'I': 1}
        r_list = [r_dict.get[i] for i in roman_string]
        for idx, char in enumerate(r_list):
            if (idx < len(r_list) - 1):
                if r_list[idx + 1] > char:
                    val -= char
                else:
                    val += char
            else:
                val += char
    return val
