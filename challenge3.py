
# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.


def contar_vocales(cadena):
    
    vocales = "aeiouAEIOU"
    contador = 0
    
    for caracter in cadena:
        
        if caracter in vocales:
            contador += 1
    
    return contador

cadena = "El minimax es un algoritmo"
numero_vocales = contar_vocales(cadena)

print(f"El número de vocales en la cadena es '{numero_vocales}'")