from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import UserCreationForm, PersonalCreationForm
from .models import Personal, Rol

class PersonalListView(ListView):
    model = Personal
    template_name = 'usuarios/personal_list.html'
    context_object_name = 'personal_list'

class PersonalCreateView(CreateView):
    model = Personal
    template_name = 'usuarios/personal_form.html'
    success_url = reverse_lazy('personal_list')

    def get(self, request, *args, **kwargs):
        user_form = UserCreationForm()
        personal_form = PersonalCreationForm()
        return render(request, self.template_name, {'user_form': user_form, 'personal_form': personal_form})

    def post(self, request, *args, **kwargs):
        user_form = UserCreationForm(request.POST)
        personal_form = PersonalCreationForm(request.POST)
        if user_form.is_valid() and personal_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            personal = personal_form.save(commit=False)
            personal.usuarios = user
            personal.contraseña = user.password
            personal.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'user_form': user_form, 'personal_form': personal_form})

class PersonalUpdateView(UpdateView):
    model = Personal
    form_class = PersonalCreationForm
    template_name = 'usuarios/personal_form.html'
    success_url = reverse_lazy('personal_list')

@login_required
def create_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        personal_form = PersonalCreationForm(request.POST)
        if user_form.is_valid() and personal_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            personal = personal_form.save(commit=False)
            personal.usuarios = user
            personal.contraseña = user.password  # Usar la contraseña encriptada del usuario
            personal.save()

            return redirect('personal_list')
    else:
        user_form = UserCreationForm()
        personal_form = PersonalCreationForm()

    return render(request, 'personal_form.html', {
        'user_form': user_form,
        'personal_form': personal_form
    })