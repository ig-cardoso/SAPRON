from django.urls import path
from . import views

urlpatterns = [
    path('calendar/<int:user_id>',views.calendar),
    path('calendar_template/<int:user_id>', views.calendar_template)
]
