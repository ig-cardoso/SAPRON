from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator 

from userCalendar.models import Controle, Checkin, Checkout, Limpeza

# Create your views here.


# tasks = Task.objects.filter(title__icontains=search, user=request.user)

def calendar(request):
    controles = Controle.objects.all() #.order_by('')
    checkins = Checkin.objects.all().order_by('data_checkin') #.order_by('hora_checkin')
    checkouts = Checkout.objects.all().order_by('data_checkout') #.order_by('hora_checkout')
    limpezas = Limpeza.objects.all().order_by('data_limpeza') #.order_by('hora_limpeza')

    # paginacao = Paginator(controles, 1)
    # page = request.GET.get('page')	
    # controles = paginacao.get_page(page) 


    return render(request, 'controle.html', {'controles': controles,
                                            'checkins': checkins,
                                            'checkouts': checkouts,
                                            'limpezas': limpezas})