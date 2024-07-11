from django import forms
from .models import Ubicacion, Stock, Estado, Consola, Distribucion, Juego



class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombreUbicacion', 'descripcion']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ubicacion', 'cantidad']

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombreEstado']

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = ['nombreConsola', 'marcaConsola']

class DistribucionForm(forms.ModelForm):
    class Meta:
        model = Distribucion
        fields = ['localidadDistribucion', 'siglaDistribucion']

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['codigo_barra', 'nombreJuego', 'consola', 'distribucion', 'imagen']

    def clean_codigo_barra(self):
        codigo_barra = self.cleaned_data.get('codigo_barra')
        if Juego.objects.filter(codigo_barra=codigo_barra).exists():
            raise forms.ValidationError("Este código de barra ya existe.")
        return codigo_barra

    def clean_nombre(self):
        nombreJuego = self.cleaned_data.get('nombre')
        if not nombreJuego:
            raise forms.ValidationError("El nombre no puede estar vacío.")
        return nombreJuego

    def clean_consola(self):
        consola = self.cleaned_data.get('consola')
        if not consola:
            raise forms.ValidationError("Debe seleccionar una consola.")
        return consola

    def clean_distribucion(self):
        distribucion = self.cleaned_data.get('distribucion')
        if not distribucion:
            raise forms.ValidationError("Debe seleccionar una distribución.")
        return distribucion

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if not imagen:
            raise forms.ValidationError("Debe subir una imagen.")
        return imagen

    def clean(self):
        cleaned_data = super().clean()
        # Agregar más validaciones aquí si es necesario
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super(JuegoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['codigo_barra'].disabled = True

    def clean_codigo_barra(self):
        codigo_barra = self.cleaned_data.get('codigo_barra')
        if not self.instance.pk and Juego.objects.filter(codigo_barra=codigo_barra).exists():
            raise forms.ValidationError("Este código de barra ya existe.")
        return codigo_barra



