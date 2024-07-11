from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Juego
from .forms import JuegoForm, StockForm
from .models import Juego, Stock
from django.urls import reverse_lazy


class JuegoListView(ListView):
    model = Juego
    template_name = 'tareas/juego_list.html'
    context_object_name = 'juego_list'

class JuegoCreateView(CreateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'tareas/juego_form.html'
    success_url = '/tareas/'  # Cambia esto según tu configuración de URL


class JuegoUpdateView(UpdateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'tareas/juego_form.html'
    success_url = '/tareas/juegos/'

def agregar_juego(request):
    if request.method == "POST":
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            juego = form.save(commit=False)
            juego.save()
            return redirect('agregar_juego')
    else:
        form = JuegoForm()
    juegos = Juego.objects.all()
    return render(request, 'tareas/juego_form.html', {'form': form, 'juegos': juegos})

def listar_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'tareas/juego_list.html', {'juego_list': juegos})


class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'tareas/stock_form.html'
    success_url = reverse_lazy('agregar_juego')

class JuegoDeleteView(DeleteView):
    model = Juego
    template_name = 'tareas/juego_confirm_delete.html'
    success_url = reverse_lazy('agregar_juego')

class JuegoEditView(UpdateView):
    model = Juego
    form_class = JuegoForm
    template_name = 'tareas/juego_edit_form.html'
    success_url = '/tareas/agregar_juego/'

    def form_valid(self, form):
        return super().form_valid(form)