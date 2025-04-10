def cantPromCom (reader,PONDERA_INDEX,II7_INDEX):
    
    emcabezado = next(reader)
    total = 0
    #cantidad que cumple con la condicion
    cantCum = 0

    for line in reader:
        total += int(line[PONDERA_INDEX])
        if line[II7_INDEX] == '1':
            cantCum += int(line[PONDERA_INDEX])
    
    #no evaluo si los valores son distintos de cero porque dicho caso es improbable
    porcentaje = (cantCum / total) * 100 
    return porcentaje

def buscarIndex (encabezado,nom):
    for i,elem in enumerate(encabezado):
        if elem == nom:
            return i

#funcion klia no me suma nada
def calcularCas (reader,IV8_INDEX,IX_TOT_INDEX,PONDERA_INDEX,AGLOMERADO_INDEX):
    dic = {}
    for line in reader:
        #pregunto si el aglomerado ya esta como clave en el diccionario
        if not line[AGLOMERADO_INDEX] in dic:
            dic[line[AGLOMERADO_INDEX]] = 0
        if line[IV8_INDEX] == 2 and line[IX_TOT_INDEX] > 2:
            dic[AGLOMERADO_INDEX] += int(line[PONDERA_INDEX])
        #print(f'AGLOMERADO:  {line[AGLOMERADO_INDEX]}, CANTIDAD: {dic[line[AGLOMERADO_INDEX]]}')    
    print (dic)
    return max(dic,key=dic.get),min(dic,key=dic.get)

