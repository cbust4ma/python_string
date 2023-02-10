# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:52:30 2023

@author: serdna
"""

import sys

if sys.argv[1].isnumeric():
    argv = int(sys.argv[1])
    if len(sys.argv) == 2:
        if argv == 0:
            print(f'zero {argv}')
        elif argv % 2 == 0:
            print (f'even {argv}') 
        else:
            print (f'odd {argv}')
    else:
        print("many arguments")
else:
    print("No Integer")



