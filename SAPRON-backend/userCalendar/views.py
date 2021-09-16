from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator 
from userCalendar.models import Locacao, Checkin, Checkout, Limpeza
import requests
import json


# Create your views here.

def calendar(request, user_id):
    '''
     Opetei por não gurdar os dados no banco, pois os dados são facilmente mutaveis.
     Pensei que o anfitreão poderá ter imóveis cadatro, então o Airbnb é quem manda o endereço no checkin.
     É preciso fazer ajustes para função funcionar.
    '''
    airbnb_request = requests.get("http://localhost:3001/usuario/"+str(user_id)) # Requisição a API fake do Airbnb
    limpezas = Limpeza.objects.all().filter(user=request.user).order_by('data_limpeza').values() # Tem que filtrar pelo id do usuário
    airbnb_dados = json.loads(airbnb_request.content)
    airbnb_dados.update({'limpeza':list(limpezas)})

    return airbnb_dados


def calendar_template(request, user_id):
    airbnb_request = requests.get("http://localhost:3001/usuario/"+str(user_id))
    airbnb_dados = json.loads(airbnb_request.content)
    limpezas = Limpeza.objects.all().order_by('data_limpeza').values().filter(user_id=user_id) 
    # Tem que filtrar pelo id do usuário
    
    return render(request, 'controle.html', {'locacao': airbnb_dados['locacao'],
                                            'limpezas': limpezas})


def calendar_teste(request):
    airbnb_request = requests.get("http://localhost:3001/teste")
    airbnb_dados = json.loads(airbnb_request.content)

    for dado_airbnb in airbnb_dados:        
        teste = Limpeza.objects.update_or_create(hora_limpeza=dado_airbnb['hora_limpeza'],
                                                data_limpeza=dado_airbnb['data_limpeza'],
                                                status_limpeza=dado_airbnb['status_limpeza'],
                                                id_limpeza=dado_airbnb['id'])
       
    locacao = Locacao.objects.all()
    checkins = Checkin.objects.all().order_by('data_checkin')
    checkouts = Checkout.objects.all().order_by('data_checkout')
    limpezas = Limpeza.objects.all().order_by('data_limpeza')

    return teste