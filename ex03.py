# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 23:13:37 2023

@author: serdna
"""

import sys
import string 

#compruebo de que haya solo dos argumentos
if  len(sys.argv) > 2:
    sys.exit ("only one parameter...") #para salir del programa y cerrar proceso a su vez

if  len(sys.argv) == 1:
    sys.exit ("Estaria bien si metes un argumento, pero tampoco te pases...")

if type(sys.argv[1]) != str:
    sys.exit("error no string")

argv = ' '.join(sys.argv[1::])
def text_analyzer(argv):
    lower = 0
    upper = 0
    space = 0
    signs = 0
    """
    Es Magia. ASi es python.... hago un contador y miro uno a uno con un bucle for
    string.punctuation
    Cadena de caracteres ASCII que se consideran caracteres de puntuación en la configuración regional C: !" #$%&'()*+,-./:;<=>?@[\]^_`{|} ~.
    """
    
    for i in argv:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper +=1
        elif i.isspace():
            space +=1
        if i in string.punctuation:
            signs += 1
    print(f'The text contains {lower + upper + space + signs} character(s)')
    print (f'-{upper} upper letter(s)\n-{lower} lower letter(s)\n-{signs} puntuation mark(s)\n-{space} space(s)')
if __name__ == '__main__':
    text_analyzer(argv)
else:
   print("He fallado lo siento hijo")