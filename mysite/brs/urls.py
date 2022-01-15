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
    path('tickets/delete/<int:number>', views.delete_ticket, name='delete_ticket'),
    path('tickets/search/', views.search_ticket, name='search_ticket'),
    path('buses/', views.bus_list, name='bus_list'),
    path('buses/<slug:slug>/',
         views.bus_detail,
         name='bus_detail'),
]