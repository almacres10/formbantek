from django.urls import path
from . import views 

app_name = 'core'

urlpatterns = [
    path('', views.formBantek, name='formBantek'),
    path('tiket/', views.tiketBantek, name='tiketBantek'),
    path('tiket/daftar/', views.daftarTiket, name='daftarTiket'),
]
