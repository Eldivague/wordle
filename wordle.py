
# se anhaden variables
letras_verificadas = []
cantidad_letras = 5

# se crea la funcion que verificara las palabras anhadidas
def verificador_palabra(palabra_ingresada, palabra_secreta):
    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i]
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta 
        
        if las_palabras_son_iguales:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append(f"({palabra_ingresada[i]})")
        else:
            letras_verificadas.append(palabra_ingresada[i])
    
    return letras_verificadas

verificador_palabra('holas', 'calor')