from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator 

from userCalendar.models import Locacao, Checkin, Checkout, Limpeza

import requests
import json

# Create your views here.


def calendar(request):
    locacao = Locacao.objects.all() #.order_by('')
    checkins = Checkin.objects.all().order_by('data_checkin') #.order_by('hora_checkin')
    checkouts = Checkout.objects.all().order_by('data_checkout') #.order_by('hora_checkout')
    limpezas = Limpeza.objects.all().order_by('data_limpeza') #.order_by('hora_limpeza')

    airbnb_request = requests.get("http://localhost:3001/teste")
    airbnb_dados = json.loads(airbnb_request.content)
    print(airbnb_dados[0]['hora_limpeza'])

    hora_limpeza_request = airbnb_dados[0]['hora_limpeza']
    data_limpeza_request = airbnb_dados[0]['data_limpeza']
    status_limpeza_request = airbnb_dados[0]['status_limpeza']

    teste = Limpeza.objects.create(hora_limpeza=hora_limpeza_request,
                                    data_limpeza=data_limpeza_request,
                                    status_limpeza=status_limpeza_request)
    

    return render(request, 'controle.html', {'locacao': locacao,
                                            'checkins': checkins,
                                            'checkouts': checkouts,
                                            'limpezas': limpezas})