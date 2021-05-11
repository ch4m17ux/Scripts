#!/usr/bin/python3
from gmpy2 import isqrt
from sys import exit

e = 0x10001
N = 16809924442712290290403972268146404729136337398387543585587922385691232205208904952456166894756423463681417301476531768597525526095592145907599331332888256802856883222089636138597763209373618772218321592840374842334044137335907260797472710869521753591357268215122104298868917562185292900513866206744431640042086483729385911318269030906569639399362889194207326479627835332258695805485714124959985930862377523511276514446771151440627624648692470758438999548140726103882523526460632932758848850419784646449190855119546581907152400013892131830430363417922752725911748860326944837167427691071306540321213837143845664837111
delta = 50

# Toma un valor x entre un rango de 1 y el exponente que le ponemos
for x in range(1, e):
    # Hace un calculo aproximado de una raiz cuadrada entre el N y el valor x encontrado, dividido en el exponente
    q_approx = isqrt(N*x//e)
    # hace un for para tratar de acercarse a los valores P y Q
    for q in range(q_approx - delta, q_approx + delta):
        if N % q == 0:
            print('P:', N/q)
            print('Q:', q)
            exit(0)
