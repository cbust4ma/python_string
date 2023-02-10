# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:42:03 2023

@author: serdna
"""

kata = (19,42,21)

print(f"the 3 numbers are: {kata[0]} {kata[1]} {kata[2]}\n")

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def get_key(val):
    for key, value in kata.items():
        if (val == value):
            return key
print(f'{get_key("Guido van Rossum")} was created by {kata.get("Python")}')
print(f'{get_key("Yukihiro Matsumoto")} was created by {kata.get("Ruby")}')
print(f'{get_key("Rasmus Lerdorf")} was created by {kata.get("PHP")}\n')


kata = (0, 4, 132.42222, 10000, 12345.67)

print(f'{round(kata[2], 2)}, {kata[3]}')