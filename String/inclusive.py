frase = input('Ingrese una frase\n')
palabras = frase.split()
frase_inclusiva = ''    

for palabra in palabras :
    silaba = -2
    if(',' in palabra):
        silaba -= 1
    if ('o' in palabra[silaba:]) :
        palabra = palabra[:silaba] + palabra[silaba:].replace('o', 'e') 
    frase_inclusiva += (palabra + ' ')

print(frase_inclusiva.strip())    
        
    
