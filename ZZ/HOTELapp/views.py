from django.shortcuts import render
from django.http import HttpResponse
from .forms import BuffetReservationForm

def bienvenidos(request):
    return HttpResponse("<h1>Bienvenidos a mi hotel</h1>")

def reserva_buffet(request):
    if request.method == 'POST':
        form = BuffetReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reserva realizada correctamente")
    else:
        form = BuffetReservationForm()
    return render(request, 'HOTELapp/reserva_buffet.html', {'form': form})