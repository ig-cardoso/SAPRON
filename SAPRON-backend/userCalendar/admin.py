from django.contrib import admin
from userCalendar.models import Locacao, Checkin, Checkout, Limpeza

# Register your models here.

# Registro do model no admin (para serem administrados)
admin.site.register(Locacao)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Limpeza)
