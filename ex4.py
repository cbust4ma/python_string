# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:17:51 2023

@author: serdna
"""

import sys

if len(sys.argv) == 1:
    sys.exit("python ex4.py 10 3 î")   
if len(sys.argv) > 2:
    sys.exit("too many arguments æ") 

if not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric() :
    sys.exit("only integers ├>") 
try:
    A = int(sys.argv[1])
    B = int (sys.argv[2])
    print(f'sum: A+B ({A + B} ♥)')
    print(f'Diff: A-B ({A - B} ♥)')
    print(f'Prod: A*B ({A * B} ♥)')
    if B == 0:
        print('Quotient: ERROR (division by zero) ☻')
        print('Quotient: ERROR (modulo by zero) ☻')
    else:
        print(f'Quotient: A/B ({A / B} ♥)')
        print(f'Remainder: A%B ({A % B} ♥)')

except:
    print("operation is impossible ♦•")