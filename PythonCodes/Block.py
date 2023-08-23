import json
import os
import numpy as np



bloque = 0
maxB = 3
valido = 0

while(bloque < maxB):

    valido = 0
    while(valido == 0):
    
        # Abre el archivo del bloque y lee los datos
        block = open('blockchain/'+str(bloque)+".json", "r+")
        data = json.load(block)
        
        
        # Obtiene el SHA-3 512 de un archivo mediante OpenSSL y lo guarda en un txt
        os.system("openssl sha3-512 blockchain/" + str(bloque) + ".json > blockchain/hash.txt")
        
        
        #Obtener el hash del archivo
        Hash = open("blockchain/hash.txt")
        digesto = Hash.read().strip()
        digesto = digesto[len(digesto)-128:]
        
        if(digesto[:2] != "00"):
            
            #Genera número aleatorio
            new_Nonce = np.random.randint(1000000000)
        
            #Modificar el Nonce del bloque
            with open('blockchain/'+str(bloque)+'.json', 'r+') as b:
                data = json.load(b)
                data['Nonce'] = str(new_Nonce) #Modifica el Nonce
                b.seek(0)        # Posición del archivo al inicio
                json.dump(data, b, indent=4)
                b.truncate()     # Eliminar parte restante
        
        else: valido = 1
    
    
    #Escribir nuevo bloque
    with open('blockchain/'+str(bloque+1)+'.json', 'w') as nb:
        nb.seek(0)        # Posición del archivo al inicio
        data['Hash'] = digesto
        json.dump(data, nb, indent=4)
        nb.truncate()     # Eliminar parte restante
    
    #Cierra el archivo
    block.close()
    
    # Aumenta en 1 el número de bloque
    bloque +=1


