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
    

    # Add ou atulza o dado de limpeza no banco de daos
    for dado_airbnb in airbnb_dados:
        teste = Limpeza.objects.update_or_create(hora_limpeza=dado_airbnb['hora_limpeza'],
                                                data_limpeza=dado_airbnb['data_limpeza'],
                                                status_limpeza=dado_airbnb['status_limpeza'],
                                                id_limpeza=dado_airbnb['id'])
    

    return render(request, 'controle.html', {'locacao': locacao,
                                            'checkins': checkins,
                                            'checkouts': checkouts,
                                            'limpezas': limpezas})