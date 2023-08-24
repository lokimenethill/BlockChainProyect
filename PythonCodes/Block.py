
import json
import os
import numpy as np



bloque = 0
maxB = 5
valido = 0

#Lee wallet pública
public = open("public_1.key").read()[27:148] 
public = public[:64] + public[65:]


while(bloque < maxB):

    #Agregando la transacción de recompensa
    #Obtener los balances del minero
    wallets = json.load(open("wallets.json", "r+"))
    balanceM = int(wallets[public])
    
    #Generando la transacción
    tran = {"Monto":"50",
            "Envia":"Recompensa",
    			"Recibe":public,
    			"Nuevo_Balance_Recibe":str(balanceM+50)}
    
    with open('blockchain/'+str(bloque)+'.json', 'r+') as b:
        data = json.load(b)
        b.seek(0)        # Posición del archivo al inicio
        data['Transacciones'] = [tran]
        json.dump(data, b, indent=4)
        b.truncate()
    b.close()
    

    #Buscando el nonce que genere un hash válido
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
            b.close()
        
        else: valido = 1
    
    #-> Actualiza balance del minero en wallets
    with open('wallets.json', 'r+') as w:
        wallets = json.load(w)
        wallets[public] = str(balanceM + 50) #Modifica el balance agregando la recompensa
        w.seek(0)        # Posición del archivo al inicio
        json.dump(wallets, w, indent=4)
        w.truncate()     # Eliminar parte restante
    w.close()
    
    #Escribir nuevo bloque
    with open('blockchain/'+str(bloque+1)+'.json', 'w') as nb:
        nb.seek(0)        # Posición del archivo al inicio
        data['Hash'] = digesto
        json.dump(data, nb, indent=4)
        nb.truncate()     # Eliminar parte restante
    nb.close()
    
    #Cierra el archivo
    block.close()
    
    # Aumenta en 1 el número de bloque
    bloque +=1


