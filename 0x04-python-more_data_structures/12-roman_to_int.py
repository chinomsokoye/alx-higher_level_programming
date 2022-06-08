#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    roman_n = 0
    for x in range(len(roman_string)):
        if x > 0 and roman_dict[roman_string[x]] > roman_dict[
                roman_string[x - 1]]:
            roman_n += roman_dict[roman_string[x]] - 2 * roman_dict[
                roman_string[x - 1]]
        else:
            roman_n += roman_dict[roman_string[x]]
    return roman_n
