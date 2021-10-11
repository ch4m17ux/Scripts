# SCRIPTS VARIOS

Aqui pretendo ir publicando scripts que me han servidor para una u otra utilidad.

## script-hash
Scripts escritos en python para obtener el hash de una cadena de texto.

Se tiene en este repositorio:

1. Script para obtener el hash MD5 de cualquier cadena de texto, que se pasara como parametro.
2. Script para obtener el hash SHA256 (adicional a MD5) de cualquier cadena de texto, que se pasara como parametro.

Ejemplo: 

```    root@kali:$  getFlag.py "Texto a codificar"```

## Script-buscar-cadena
Script en Python para buscar una cadena de texto dentro un fichero comprimido tar.gz

Ejemplo de Uso:

```python3 buscar-cadena-tar.py "texto a buscar" fichero.tar.gz```

## Script-generar-p_q-RSA
Script en pyhton que genera los valores p y q, de un cifrado RSA, teniendo el exponente y el valor N.

Ejemplo:
```
# Se debe tener el exponente y la N, para poder calcular los valores p y q.
e = 0x10001
N = 16809924442712290290403972268146404729136337398387543585587922385691232205208904952456166894756423463681417301476531768597525526095592145907599331332888256802856883222089636138597763209373618772218321592840374842334044137335907260797472710869521753591357268215122104298868917562185292900513866206744431640042086483729385911318269030906569639399362889194207326479627835332258695805485714124959985930862377523511276514446771151440627624648692470758438999548140726103882523526460632932758848850419784646449190855119546581907152400013892131830430363417922752725911748860326944837167427691071306540321213837143845664837111
delta = 50
```

## Script rsatool.py
rsatool calcula los parametros RSA (p, q, n, d, e) and RSA-CRT (dP, dQ, qInv) dados dos primos (p, q) o modulo y exponente privado (n, d).

Los parámetros resultantes se muestran y, opcionalmente, se pueden escribir como una clave privada RSA codificada en PEM o DER compatible con OpenSSL.

Ejemplos:

Supliendo modulo y exponente privador, salida PEM a key.pem:

```python rsatool.py -f PEM -o key.pem -n 13826123222358393307 -d 9793706120266356337```

Supliendo dos primos, Salida DER a key.der:

```python rsatool.py -f DER -o key.der -p 4184799299 -q 3303891593```

## Script dnadecode.py
Script que decodifica un string en cifrado DNA a caracteres ascii:

Ejemplo:

se debe digitar la cadena a descifrar dentro del script:

```
...
string = 'GCGCCAAAGACTTTCTTGCTACACCGAATTCATTTC'
...
```

Ejecutar el script
```python2 dnacode.py```

## Script decode_bacon.py
Script que decodifica un string en cifrado bacon.

## Script request.py
Script que saca los datos de una web y extrae la informacion para sumar dos numeros, enviando la respuesta. Reto de PaellaCTF donde se nos pedia sumar rapidamente dos numeros y enviar el resultado antes de 5 segundos para obtener la flag.
