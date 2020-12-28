#!/usr/bin/python3

import hashlib
import sys
 
#s = hashlib.sha256()
#s.update(b"ThisIsAMoreSecureHashFunction")
#m = hashlib.md5()
#m.update(s.hexdigest().encode('utf-8'))
#print("flag{"+m.hexdigest()+"}")

if len(sys.argv) == 2:
	hashsha256 = hashlib.sha256()
	hashsha256.update(b"ThisIsAMoreSecureHashFunction")
	hashmd5 = hashlib.md5()
	hashmd5.update(hashsha256.hexdigest().encode('utf-8'))

	print ('sha256: ' + hashsha256.hexdigest() + '')
	print("flag{" + hashmd5.hexdigest() + "}")
else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: sha256.py "Texto a codificar"')
