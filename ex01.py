# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:34:27 2023

@author: serdna
"""

import sys

#une los argumentos con espacios simples ( ' ') entre ellos.
#empieza al reves [::-1] hasta llegar a 0
argv = ' '.join(sys.argv[1::])[::-1]

#El swapcase()método devuelve una cadena donde todas las letras mayúsculas son minúsculas y viceversa.
print(argv.swapcase())