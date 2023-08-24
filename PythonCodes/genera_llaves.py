#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:13:54 2023

@author: balam
"""

import json
import os
import requests



#Crea pares de llaves, privada y pública (wallet)
def genera_llaves():
    os.system("openssl ecparam -name secp256k1 -genkey -out private.key ")
    os.system("openssl ec -in private.key -pubout -out public.key")
    
    URL = f'http://192.168.2.{i}/addnode?sdfg='
    requests.get(URL)


    

#Transacción

#private = open("private.key").read()[102:264] #Lee wallet private
#public = open("public.key").read()[27:148] #Lee wallet pública



# #Obtiene los datos del bloque (json)
# block = open("1_pruebas.json", "r+")
# data = json.load(block)



def genera_transaccion(envia, recibe, monto):
    #Transacciones en el bloque
    #transacciones = data['Transacciones']
    
    #Obtener los balances del que Envía y del que Recibe de Wallets
    wallets = json.load(open("wallets.json", "r+"))
    balanceE = int(wallets[envia])
    balanceR = int(wallets[recibe])
    
    #Verifica que tiene fondos la wallet que envia
    if balanceE < monto:
        print("No hay fondos suficientes")
        return
    
    #Generando la transacción
    tran = {"Monto":str(monto),
            "Envia":str(envia),
    			"Nuevo_Balance_Envia":str(balanceE-monto),
    			"Recibe":str(recibe),
    			"Nuevo_Balance_Recibe":str(balanceR+monto),
    			"Firma":""}
    
    #Genera un archivo con la descripción de la transacción
    with open("transaccion.txt", "w") as archivo:
        archivo.write("Envia:"+tran['Envia'])
        archivo.write("\n")
        archivo.write("Nuevo_Balance_Envia:"+tran['Nuevo_Balance_Envia'])
        archivo.write("\n")
        archivo.write("Recibe:"+tran['Recibe'])
        archivo.write("\n")
        archivo.write("Nuevo_Balance_Recibe:"+tran['Nuevo_Balance_Recibe'])
    archivo.close()
       
    
    #Genera un archivo con la firma de la transacción
    os.system("openssl sha3-512 transaccion.txt > hash_transaccion.txt")
    #print()
    os.system("openssl dgst -sha256 -sign private_1.key -out firma.signature hash_transaccion.txt")
    #print()
    os.system("base64 firma.signature > firma.txt")

    #Abre el archivo txt con la firma
    firma = open('firma.txt').read()
    #print(firma)
    
    #Coloca el hash de la firma en la estructura de la transacción
    tran['Firma'] = firma
    
    
    with open('2_pruebas.json', 'r+') as b:
        data = json.load(b)
        data['Transacciones'] += [tran] #Modifica el Nonce
        b.seek(0)        # Posición del archivo al inicio
        json.dump(data, b, indent=4)
        b.truncate()     # Eliminar parte restante


    #Actualiza el balance en el archivo Wallets
    with open('wallets.json', 'r+') as b:
        data = json.load(b)
        data[envia] = str(balanceE - monto) #Modifica el Nonce
        data[recibe] = str(balanceR + monto) #Modifica el Nonce
        b.seek(0)        # Posición del archivo al inicio
        json.dump(data, b, indent=4)
        b.truncate()     # Eliminar parte restante


 
envia = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEbGFqyGvH4P/wqjT9rl0hLuH37lXl1dbHCQ01guFOlBU/RtGyBw6k+uOlFZT3VPKQwHQoAzpLp2Wl94ZSMe1gHg=="
recibe = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEEKDehofm2sRsh1GKKoRNLdwRAk6snu3Psk2b4XG5cimY0OlCXVy2qSSF/wfZ1ak4ZeVw3ieykXahzVp8OPWD2w=="

genera_transaccion(envia, recibe, 10)




