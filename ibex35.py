
# coding: utf-8

# In[11]:


#Libraries
import os
import requests
import csv
import argparse
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup

EcoUrl="http://www.eleconomista.es/indice/IBEX-35/historico-fechas"
currentDate=''
headerValues={}
formData={}
#Set the header values of HTTP Request
headerValues['Origin']='http://www.eleconomista.es'
headerValues['Referer']='http://www.eleconomista.es/indice/IBEX-35/historico-fechas'
headerValues['Content-Type']='application/x-www-form-urlencoded'
headerValues['X-Requested-With']='XMLHttpRequest'
headerValues['x-elastica_gw']='2.43.0'

formData={}

#Set the POST values of HTTP Request

formData['dia_desde']='19'
formData['mes_desde']='03'
formData['ano_desde']='2018'

formData['dia_hasta']='23'
formData['mes_hasta']='03'
formData['ano_hasta']='2018'

formData['intervalo']='/indice/IBEX-35/historico-fechas/'
formData['action=']='../cotizacion/index.php?nombre=IBEX%2035&vista=historialaccion&orden=siguiente'

response= requests.post(EcoUrl, params = formData, headers=headerValues)
#<input class="button radius small right" name="enviar" type="button" value="Ver" onclick="reenvia()"/

soup = BeautifulSoup(response.text,"html.parser")
tablehistoricos=soup.find("table",{"class":"tablapeq tablag tablehistoricos"})
elementList=[]
data_Ibex=[0]*6

for row in tablehistoricos.findAll("tr"):
    cells = row.findAll('td')
    if (len(cells)==7):
        for k in range(0,6):
            data_Ibex[k]=cells[k].find(text=True)
        elementList.append(data_Ibex)

elementList

