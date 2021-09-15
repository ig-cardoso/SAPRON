from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator 

from userCalendar.models import Locacao, Checkin, Checkout, Limpeza

import requests

# Create your views here.


def calendar(request):
    locacao = Locacao.objects.all() #.order_by('')
    checkins = Checkin.objects.all().order_by('data_checkin') #.order_by('hora_checkin')
    checkouts = Checkout.objects.all().order_by('data_checkout') #.order_by('hora_checkout')
    limpezas = Limpeza.objects.all().order_by('data_limpeza') #.order_by('hora_limpeza')

    Airbnb_request = requests.get("http://localhost:3001/teste")
    print(Airbnb_request)

    teste = Limpeza.objects.create(hora_limpeza="23:30", data_limpeza="12/02/2021", status_limpeza='Fazendo')
    

    return render(request, 'controle.html', {'locacao': locacao,
                                            'checkins': checkins,
                                            'checkouts': checkouts,
                                            'limpezas': limpezas})