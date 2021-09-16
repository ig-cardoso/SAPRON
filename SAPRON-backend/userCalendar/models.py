from django.db import models
from django.contrib.auth.models import User
from django.db.models import manager
from djmoney.models.fields import MoneyField  # É preciso instalar esse módulo


# Create your models here.

STATUS = (
		('fazendo', 'Fazendo'),
		('feito', 'Feito')
	)

class Locacao(models.Model):
    id_locacao = models.AutoField(primary_key=True)
    checkin = models.ForeignKey('Checkin', on_delete=models.CASCADE, related_name='checkin')
    checkout = models.ForeignKey('Checkout', on_delete=models.CASCADE, related_name='checkout')
    limpeza = models.ForeignKey('Limpeza', on_delete=models.CASCADE, related_name='limpeza')
    codigo_reserva = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    nome_usuario = models.CharField(max_length=50)
    numero_usuario = models.CharField(max_length=25)
    quatidade_adultos = models.IntegerField(blank=False)
    quatidade_criancas = models.IntegerField(blank=False)
    quantidade_pet = models.IntegerField(blank=False)
    quantidade_diarias = models.IntegerField(blank=False)
    valor_a_pagar = MoneyField(decimal_places=0, default=0.0, default_currency='USD', max_digits=11,)
    ja_pago = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return str(self.id_locacao)

    class Meta:
        # manager = True
        db_table = 'Locacao'
        verbose_name_plural = u'Locacoes' 


class Checkin(models.Model):
    id_checkin = models.IntegerField(primary_key=True, blank=False)
    data_checkin = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    hora_checkin = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=True)
    status = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return str(self.id_checkin)

    class Meta:
        # manager = True
        db_table = 'CheckIn'
        verbose_name_plural = u'Checkins' 


class Checkout(models.Model):
    id_checkout = models.IntegerField(primary_key=True, blank=False)
    data_checkou = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    hora_checkou = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=True)
    status = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return str(self.id_checkout)

    class Meta:
        # manager = True
        db_table = 'Checkout'
        verbose_name_plural = u'Checkouts' 


class Limpeza(models.Model):
    # id_limpeza = models.IntegerField(primary_key=True, blank=False)  # id manual
    id_limpeza = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=False, null=True) # Provisório
    hora_limpeza = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=True)
    data_limpeza = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    status_limpeza = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return str(self.id_limpeza)

    class Meta:
        # manager = True
        db_table = 'Limpeza'
        verbose_name_plural = u'Limpezas'