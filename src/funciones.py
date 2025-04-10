def cantMujHom (reader, CH04_INDEX, PONDERA_INDEX):
    """
    Esta funcion recibe un archivo csv y dos indices de columnas, y devuelve la cantidad de hombres y mujeres
    """
    # guardo el encabezado para ir a la siguiente linea
    encabezado = next(reader) 
    contador_f = 0
    contador_m = 0

    #recorre tambien la PRIMERA linea del archivo, que es la que tiene los nombres de las columnas
    for line in reader:
        #print(line)
        #imprimo la primera columna de cada fila
        
        if line[CH04_INDEX] == '1':
            # lo debo convertir a integer porque el dato es en realidad un string
            contador_m += int(line[PONDERA_INDEX])
        else:
            contador_f += int(line[PONDERA_INDEX])

    #pareciera como si me hubiera creado una lista directamente con todos los elementos de cada fila del archivo
    return(contador_f, contador_m)


def termSec (reader,NIVEL_ED_INDEX,CH06_INDEX,PONDERA_INDEX):

    def cumple (line,NIVEL_ED_INDEX,CH06_INDEX):
        if (line[CH06_INDEX] > '18') and (line[NIVEL_ED_INDEX] == '4' or line[NIVEL_ED_INDEX] == '5' or line[NIVEL_ED_INDEX] == '6'):
            return True
        else:
            return False

    encabezado = next(reader)

    cantSecCom = 0

    for line in reader:
        if cumple(line,NIVEL_ED_INDEX,CH06_INDEX):
            cantSecCom += int(line[PONDERA_INDEX])
    return(cantSecCom)
