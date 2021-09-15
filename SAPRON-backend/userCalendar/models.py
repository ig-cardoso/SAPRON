from django.db import models
from django.contrib.auth.models import User
from django.db.models import manager

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

    def __str__(self):
        return str(self.id_locacao)

    class Meta:
        # manager = True
        db_table = 'Locacao'
        verbose_name_plural = u'Locacoes' 


class Checkin(models.Model):
    id_checkin = models.AutoField(primary_key=True)
    hora_checkin = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=True)
    data_checkin = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    responsavel_checkin = models.CharField(max_length=100)
    status_checkin = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return str(self.id_checkin)

    class Meta:
        # manager = True
        db_table = 'CheckIn'
        verbose_name_plural = u'Checkins' 


class Checkout(models.Model):
    id_checkout = models.AutoField(primary_key=True)
    hora_checkout = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=True)
    data_checkout = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    responsavel_checkout = models.CharField(max_length=100)
    status_checkout = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return str(self.id_checkout)

    class Meta:
        # manager = True
        db_table = 'Checkout'
        verbose_name_plural = u'Checkouts' 


class Limpeza(models.Model):
    id_limpeza = models.AutoField(primary_key=True)
    hora_limpeza = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=True)
    data_limpeza = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    status_limpeza = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return str(self.id_limpeza)

    class Meta:
        # manager = True
        db_table = 'Limpeza'
        verbose_name_plural = u'Limpezas'