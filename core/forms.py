from django import forms
from django.core.exceptions import ValidationError
from .models import Libro, Cliente, Pedido

class CrearLibroForm(forms.Form):
    id = forms.IntegerField(label="Ingresa el ID", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    ISBN = forms.IntegerField(label="Ingresa el ISBN", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    titulo = forms.CharField(label="Ingresa el Título", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    autor = forms.CharField(label="Ingresa el Autor", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    precio = forms.IntegerField(label="Ingresa el Precio", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    # mensaje = forms.CharField(
    #     label="Escribe Tu Mensaje",
    #     required=True,
    #     widget=forms.Textarea(attrs={"class":"field"}))

    def clean_ISBN(self):
        ISBN = str(self.cleaned_data["ISBN"])
        if len(ISBN) != 13:
            raise ValidationError("❌El ISBN debe contener 13 dígitos")
        return self.cleaned_data["ISBN"]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     nombre = cleaned_data.get("nombre")
    #     apellido = cleaned_data.get("apellido")
    #     if nombre == "Carlos" and apellido == "Lopez":
    #         raise ValidationError("❌El Usuario ya envio un Mensaje")
    #     return self.cleaned_data

class ModificarLibroModelForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"

    def clean_ISBN(self):
        ISBN = str(self.cleaned_data["ISBN"])
        if len(ISBN) != 13:
            raise ValidationError("❌El ISBN debe contener 13 dígitos")
        return self.cleaned_data["ISBN"]



class CrearClienteForm(forms.Form):
    id = forms.IntegerField(label="Ingresa el ID", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    dni = forms.IntegerField(label="Ingresa el DNI", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    nombre = forms.CharField(label="Ingresa el Nombre", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    apellido = forms.CharField(label="Ingresa el Apellido", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    email = forms.EmailField(label="Ingresa el Email", required=True, widget=forms.TextInput(attrs={"class":"field"}))

    def clean_dni(self):
        DNI = str(self.cleaned_data["dni"])
        if len(DNI) != 8:
            raise ValidationError("❌El DNI debe contener 8 dígitos")
        return self.cleaned_data["dni"]

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("❌El Nombre solo puede estar contener letras")
        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("❌El Apellido solo puede estar contener letras")
        return self.cleaned_data["apellido"]

class ModificarClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
    
    def clean_dni(self):
        DNI = str(self.cleaned_data["dni"])
        if len(DNI) != 8:
            raise ValidationError("❌El DNI debe contener 8 dígitos")
        return self.cleaned_data["dni"]

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("❌El Nombre solo puede estar contener letras")
        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("❌El Apellido solo puede estar contener letras")
        return self.cleaned_data["apellido"]



class CrearPedidoForm(forms.Form):
    id = forms.IntegerField(label="Ingresa el ID", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    pedido = forms.CharField(label="Ingresa el Pedido", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    cliente = forms.CharField(label="Ingresa el Cliente", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    libro = forms.CharField(label="Ingresa el Libro", required=True, widget=forms.TextInput(attrs={"class":"field"}))    
    fechaPedido = forms.DateField(label="Ingresa la Fecha del Pedido", required=True, widget=forms.TextInput(attrs={"class":"field"}))
    cantidad = forms.IntegerField(label="Ingresa la Cantidad", required=True, widget=forms.TextInput(attrs={"class":"field"}))