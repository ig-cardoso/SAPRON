from django.db import models
from django.contrib.auth.models import User
from django.db.models import manager
# from userCalendar.models import Limpeza

# Create your models here.

class Anfitriao(models.Model):
    id_anfitriao = models.AutoField(primary_key=True)
    cpd_anfitriao = models.CharField(max_length=11, null=False, blank=False)
    name_anfitriao = models.CharField(max_length=50)
    date_year_anfitriao = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=True)
    email_anfitriao = models.CharField(max_length=30, null=False, blank=False)

    # limpeza = models.ForeignKey('userCalendar.Limpeza', on_delete=models.CASCADE, related_name='limpeza')

    # Tem outros campos

    def __str__(self):
        return str(self.id_anfitriao)

    class Meta:
        # manager = True
        db_table = 'Anfitriao'
        verbose_name_plural = u'Anfitrioes' 
