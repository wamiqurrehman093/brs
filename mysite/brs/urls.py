from django.urls import path
from . import views

app_name = 'brs'

urlpatterns = [
    # post views
    path('', views.main, name='main'),
    path('booking/', views.booking, name='booking'),
    path('cancellation/', views.cancellation, name='cancellation'),
    path('status/', views.status, name='status'),
    path('tickets/<slug:slug>', views.ticket_detail, name='ticket_detail'),
    path('buses/', views.bus_list, name='bus_list'),
    path('buses/<slug:slug>/',
         views.bus_detail,
         name='bus_detail'),
]