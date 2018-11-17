'''
Created on 16/11/2018

@author: acer
'''

def ordenamientoSeleccion(numeros):
    import time
    inicio = time.time()
    for recorrido in range(len(numeros)-1, 0, -1):
        posicionMayor = 0;
        for recorrido2 in range (1, recorrido +1):
            if numeros[recorrido2] > numeros[posicionMayor]:
                posicionMayor = recorrido2
                
        aux = numeros[recorrido]
        numeros[recorrido] = numeros[posicionMayor]
        numeros[posicionMayor] = aux
    final = time.time()
    tiempo = round(final - inicio)
    #print("Tiempo de ejecucion: " + tiempo)
    
a = [7, 1, 3, 5, 9, 2, 3] 
print("Lista sin ordenar: ")
print(a)
print()        
ordenamientoSeleccion(a)  
print("Lista ordenada: ")
print(a)