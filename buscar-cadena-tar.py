import tarfile
import sys

found = []

with tarfile.open(sys.argv[2], "r:gz") as t:
  for elem in t:
    if not elem.isfile():
       continue
    f = t.extractfile(elem)
    for n, linea in enumerate(f):
        if sys.argv[1].encode("utf-8") in linea:
           # print("{}:{} {}".format(elem.name, n, linea))
           found.append(elem.name)
           break

if not found:
    print("La cadena no aparece en ningún fichero")
    quit()

print("Cadena encontrada en los siguientes ficheros")
for filename in found:
    print(filename)
