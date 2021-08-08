
**  *Debajo se encunentran algunos ejercicios de la cursada***


------------

### Ejercicio 1.4: Debuguear
El siguiente fragmento de código está relacionado con el problema del obelisco. Tiene un bug, es decir, un error.

```python
# obelisco.py

grosor_billete = 0.11 * 0.001 # 0.11 mm en metros
altura_obelisco = 67.5         # altura en metros
num_billetes = 1
dia = 1

while num_billetes * grosor_billete <= altura_obelisco:
    print(dia, num_billetes, num_billetes * grosor_billete)
    dia = dias + 1
    num_billetes = num_billetes * 2

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final', num_billetes * grosor_billete)
```

Copiá y pegá el código que aparece arriba en un nuevo archivo llamado `obelisco.py`. Cuando ejecutes el código vas a obtener el siguiente  mensaje de error que hace que el programa se detenga:

```code
Traceback (most recent call last):
  File "obelisco.py", line 10, in <module>
    dia = dias + 1
NameError: name 'dias' is not defined
```

Aprender a leer y entender los mensajes de error es una parte fundamental de programar en Python. Si tu programa *crashea* (se rompe, da error) la última línea del mensaje de error indica el motivo. Un poco más arriba vas a ver un fragmento de código, un nombre de archivo y un número de línea que identifican el problema.

* ¿En qué linea está el error?
* ¿Cuál es el error?
* Repará el error.
* Ejecutá el programa exitosamente.


### Ejercicio 1.5: La pelota que rebota
Este es el primer conjunto de ejercicios en el que vas a tener que crear un archivo de Python y correrlo. A partir de aca, vamos a asumir que estás trabajando en el subdirectorio `ejercicios_python/`. Para ayudarte a organizar los archivos de diferentes clases y a ubicar el lugar correcto ya creamos algunos subdirectorios y un par de archivos en el directorio correpondiente a esta clase. Buscá en tu terminal el archivo `ejercicios_python/Clase01/rebotes.py` (cambiando de directorio como vimos recién). Lo vamos a usar en este ejercicio. 

Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa `rebotes.py` que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

Tu programa debería generar una tabla que se parezca a esta:

```code
1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
```

### Ejercicio 1.6: Saludos
Escribí un programa llamado `saludo.py` que pregunte el nombre de le usuarie, imprima un saludo (por ejemplo, "Hola, Juana") y termine.

### Ejercicio 1.7: La hipoteca de David
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:

```python
# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))
```

Copiá este código y correlo. Deberías obtener `966279.6` como respuesta.

### Ejercicio 1.8: Adelantos
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.

Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.

Cuando lo corras, este nuevo programa debería dar un pago total de  `929965.62` en 342 meses.

Aclaración: aunque puede parecer sencillo, este ejercicio requiere que agregues una variable *mes* y que prestes bastante atención a cuándo la incrementás, con qué valor entra al ciclo y con qué valor sale del ciclo. Una posiblidad es inicializar *mes* en 0 y otra es inicializarla en 1. En el primer caso es problabl que la variable salga del ciclo contando la cantidad de pagos que se hicieron, en el segundo, ¡es probable que salga contando la cantidad de pagos más uno!

### Ejercicio 1.9: Calculadora de adelantos
¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?

Modificá tu programa de forma que la información sobre pagos extras sea incorporada de manera versátil. Agregá las siguientes variables antes del ciclo, para definir el comienzo, fin y monto de los pagos extras:

```python
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
```

Hacé que el programa tenga en cuenta estas variables para calcular el total a pagar apropiadamente.

### Ejercicio 1.10: Tablas
Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante. La salida debería verse aproximadamente así:

```bash
1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total pagado:  880074.1
Meses:  310
```

### Ejercicio 1.11: Bonus
Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

### Ejercicio 1.17: Iteración sobre cadenas
Usá el comando `for` para iterar sobre los caracteres de una cadena.

```python
>>> cadena = "Ejemplo con for"
>>> for c in cadena:
        print('caracter:', c)
# Mirá el output.
```

Modificá el código anterior de manera que dentro del ciclo el programa cuente cuántas letras "o" hay en la cadena.


### Ejercicio 1.18: Geringoso rústico
Usá una iteración sobre el string `cadena` para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

```python
>>> cadena = 'Geringoso'
>>> capadepenapa = ''
>>> for c in cadena:
        ?
>>> capadepenapa
Geperipingoposopo
```
Podés probar tu código cambiando la cadena inicial por otra palabra, como 'apa' o 'boligoma'.

Guardá el código en un archivo `geringoso.py`.


