import json
import os
import requests
import time


#Crea pares de llaves, privada y pública (wallet)
def genera_llaves():
    os.system("openssl ecparam -name secp256k1 -genkey -out private.key ")
    os.system("openssl ec -in private.key -pubout -out public.key")
    public = open("public.key").read()[27:148] 
    public = public[:64] + public[65:]
    '''
    for i in range(1,255):
        URL = f'http://192.168.2.{i}/recibeWallet?pk={public}'
        requests.get(URL)
        time.sleep(1)
    '''
genera_llaves()
URL = f'http://192.168.129.123:10109/recibeWallet?pk=dasd'
res = requests.get(URL,timeout=0.500)
