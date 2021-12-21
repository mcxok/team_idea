from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
# Create your views here.


def index(request):
    result = ''
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    soup = BeautifulSoup(response.content, 'html.parser')
    soup1 = float(soup.find(id='R01135').find('value').get_text().replace(',','.'))
##    soup1 = soup1.find('value')
##    soup1 = soup1.get_text()
##    soup1 = soup1.replace(',','.')
##    soup1 = float(soup1)

    soup2 = float(soup.find(id='R01535').find('value').get_text().replace(',', '.'))
##    soup2 = soup2.find('value')
##    soup2 = soup2.get_text()
##    soup2 = soup2.replace(',', '.')
##    soup2 = float(soup2)

    res = round(soup2 / soup1, 4)
    result += f'Стоимость норвежской кроны {res} венгерских форинтов'
    return HttpResponse(result)