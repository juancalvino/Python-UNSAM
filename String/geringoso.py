cadena = input('Ingresa una palabra\n')
geringoso = ''

for c in cadena:
    if(c in 'aeiou'):
        c += 'p' + c
    geringoso += c

print(cadena,'en geringoso se dice',geringoso)
    
