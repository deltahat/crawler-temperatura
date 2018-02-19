# -*- coding: utf-8 -*-

# Importaciones
from bs4 import BeautifulSoup
import requests
import time
import os

#Bucle infinito
#while True:

# Captura de url
url = "http://www.timeanddate.com/weather/argentina/cordoba"

# Captura de hml y creacion de un objeto Response
r  = requests.get(url)
data = r.text

# Creacion del objeto soup y envio de lo acpturado
soup = BeautifulSoup(data, 'lxml')

# Busqueda del div para obtecion de temperatura
temp = soup.find_all('div', class_="h2")

# Busqueda del div para obtecion de sensacion termica
sTerm = soup.find_all('div', class_="clear")

# [0] es el primer elemento y [1] el segundo
print("El dia de hoy")
print ("La temperatura en Cordoba: ") + temp[0].text
print ("La sesacion termica: ") + sTerm[1].text

# Tiempo en segundos para la proxima ejecucion
time.sleep(15)

# Borrado de datos antiguos
os.system("clear")
