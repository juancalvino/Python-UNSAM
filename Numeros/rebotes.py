#Tradicional
altura = 100
rebotesTotales = 10

while(rebotesTotales > 0):
    altura *= (3/5)
    rebotesTotales -= 1
    print(round(altura,4))

print("----------------------")

#Recursivo
def getValoresEnRebotes(alturaS, cantidadDeRebotes = 10):
    if(cantidadDeRebotes <= 0):
        return alturaS
    alturaS *= (3 / 5)
    cantidadDeRebotes -= 1
    print(round(alturaS, 4))
    getValoresEnRebotes(alturaS,cantidadDeRebotes)

getValoresEnRebotes(100)

print("----------------------")

getValoresEnRebotes(20,3)
