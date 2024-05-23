from django import forms
from django.core.exceptions import ValidationError

class contactoForm(forms.Form):
    nombre = forms.CharField(label="Ingresa Nombre", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    apellido = forms.CharField(label="Ingresa Apellido", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    telefono = forms.IntegerField(label="Ingresa Teléfono", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    email = forms.EmailField(label="Ingresa Correo Electrónico", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    mensaje = forms.CharField(
        label="Escribe Tu Mensaje",
        required=True,
        widget=forms.Textarea(attrs={"class":"field"}))

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "")
        if not nombre.isalpha():
            raise ValidationError("❌El Nombre solo puede contener letras")
        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        apellido = self.cleaned_data.get("apellido", "")
        if not apellido.isalpha():
            raise ValidationError("❌El Apellido solo puede contener letras")
        return self.cleaned_data["apellido"]
    
    def clean_telefono(self):
        telefono = str(self.cleaned_data["telefono"])
        if len(telefono) != 10:
            raise ValidationError("❌El Teléfono debe contener 10 dígitos")
        return self.cleaned_data["telefono"]

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        if nombre == "Carlos" and apellido == "Lopez":
            raise ValidationError("❌El Usuario ya envio un Mensaje")
        return self.cleaned_data