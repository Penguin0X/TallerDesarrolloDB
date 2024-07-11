
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Personal
import re

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya existe.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("La contraseña debe tener al menos una letra mayúscula.")
        if not re.search(r'[a-z]', password):
            raise ValidationError("La contraseña debe tener al menos una letra minúscula.")
        if not re.search(r'\d', password):
            raise ValidationError("La contraseña debe tener al menos un número.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("La contraseña debe tener al menos un símbolo especial.")
        return password

class PersonalCreationForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('nombrePersonal', 'rol', 'telefono', 'contraseña')

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit() or len(telefono) != 8:
            raise forms.ValidationError("El teléfono debe ser un número de 8 dígitos.")
        return telefono
