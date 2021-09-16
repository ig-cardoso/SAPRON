from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator 

from userCalendar.models import Locacao, Checkin, Checkout, Limpeza

import requests
import json
import pprint


# Create your views here.

def calendar(request):
    # Opetei por não gurdar os dados no banco, pois os dados são facilmente mutaveis
    # Pensei que o anfitreão poderá ter imóveis cadatro, então o Airbnb é quem manda o endereço no checkin
    user_id = 222
    airbnb_request = requests.get("http://localhost:3001/usuario/"+str(user_id)) # Requisição a API fake do Airbnb
    airbnb_dados = json.loads(airbnb_request.content)
    
    limpezas = Limpeza.objects.all().order_by('data_limpeza')#.filter(id_limpeza=user_id) # Tem que filtrar pelo id do usuário
    

    pprint.pprint(airbnb_dados)


    return render(request, 'controle.html', {'locacao': airbnb_dados['locacao'],
                                            'limpezas': limpezas})
    # return airbnb_dados



def calendar_(request):
    airbnb_request = requests.get("http://localhost:3001/teste")
    airbnb_dados = json.loads(airbnb_request.content)
    
    # Add ou atulza o dado de limpeza no banco de daos

    for dado_airbnb in airbnb_dados:
        
        teste = Limpeza.objects.update_or_create(hora_limpeza=dado_airbnb['hora_limpeza'],
                                                data_limpeza=dado_airbnb['data_limpeza'],
                                                status_limpeza=dado_airbnb['status_limpeza'],
                                                id_limpeza=dado_airbnb['id'])
       
    locacao = Locacao.objects.all() #.order_by('')
    checkins = Checkin.objects.all().order_by('data_checkin') #.order_by('hora_checkin')
    checkouts = Checkout.objects.all().order_by('data_checkout') #.order_by('hora_checkout')
    limpezas = Limpeza.objects.all().order_by('data_limpeza') #.order_by('hora_limpeza')

    return teste