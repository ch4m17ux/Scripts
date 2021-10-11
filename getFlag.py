#!/usr/bin/python3

import hashlib
import sys

#hashmd5 = hashlib.md5()
#stexto = input()
#hashmd5.update(stexto.encode())

#print ('flag{' + hashmd5.hexdigest() + '}')


if len(sys.argv) == 2:
    hashmd5 = hashlib.md5()
    stexto = sys.argv[1]
    hashmd5.update(stexto.encode())
    print ('PaellaCTF{' + hashmd5.hexdigest() + '}')
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: getFlag.py "Texto a codificar"')
