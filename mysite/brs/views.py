from datetime import datetime
import imp
from django.http import HttpResponseRedirect
from time import timezone
from xmlrpc.client import DateTime
from django.shortcuts import render, get_object_or_404
from .models import Bus, Ticket
from .forms import TicketForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

# Create your views here.
def main(request):
    return render(request, 'brs/main.html', {})

def booking(request):
    new_ticket = None
    error = ''
    if request.method == 'POST':
        ticket_form = TicketForm(data=request.POST)
        if ticket_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            bus = ticket_form.cleaned_data['bus']
            if new_ticket.booked_seats == 0:
                error = 'You can not book 0 seats'
                return render(request, 'brs/booking.html', {'ticket_form': ticket_form, 'error': error})
            if bus.available_seats < new_ticket.booked_seats:
                error = 'This many seats are not available.'
                return render(request, 'brs/booking.html', {'ticket_form': ticket_form, 'error': error})
            bus.available_seats -= new_ticket.booked_seats
            bus.save()
            name = ticket_form.cleaned_data['name'].replace(' ', '-').lower()
            ticket_date = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            new_ticket.slug = name + "-" + ticket_date
            new_ticket.save()
            return HttpResponseRedirect(new_ticket.get_absolute_url())
            #return render(request, 'brs/booked.html', {'ticket': new_ticket, 'error': error})
    else:
        ticket_form = TicketForm()
    return render(request, 'brs/booking.html', {'ticket_form': ticket_form})

def cancellation(request):
    return render(request, 'brs/cancellation.html', {})

def status(request):
    return render(request, 'brs/status.html', {})

def bus_list(request):
    object_list = Bus.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        buses = paginator.page(page)
    except PageNotAnInteger:
        buses = paginator.page(1)
    except EmptyPage:
        buses = paginator.page(paginator.num_pages)
    return render(request, 'brs/bus/list.html', {'page': page, 'buses': buses})

def bus_detail(request, slug):
    bus = get_object_or_404(Bus, slug=slug)
    return render(request, 'brs/bus/detail.html', {'bus': bus})

def ticket_detail(request, slug):
    ticket = get_object_or_404(Ticket, slug=slug)
    return render(request, 'brs/ticket/detail.html', {'ticket': ticket})