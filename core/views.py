from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import *
from .models import Libro, Cliente, Pedido
<<<<<<< HEAD
=======
import datetime
>>>>>>> 160abb9fe1466c2f9be5777c6ddafefea10af58b

# Create your views here.
# def index(request):
#     return HttpResponse('HolaMundo')

# def ventas(request):
#     libros=[Libro("Python Crash Course: A Hands-On, Project-Based Introduction to Programming","Eric Matthes","Programación","No Starch Press",2019),
#             Libro("Automate the Boring Stuff with Python: Practical Programming for Total Beginners","Al Sweigart","Programación","No Starch Press",2019),
#             Libro("Fluent Python: Clear, Concise, and Effective Programming","Luciano Ramalho","Programación","O'Reilly Media",2015),
#             Libro("Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython","Wes McKinney","Ciencia de Datos","O'Reilly Media",2017),
#             Libro("Effective Python: 90 Specific Ways to Write Better Python","Brett Slatkin","Programación","Addison-Wesley Professional",2015)]
#     context = { "libros":libros }
#     return render(request, "core/pages/get_libros.html",context)

def index(request):
    contexto = {
        'fecha_hora': datetime.datetime.now()
    }
    return render(request, 'core/index.html', contexto)

def user_logout(request):
    logout(request)
    messages.success(request, '✔️Sesión Cerrada con ÉXITO')
    return render(request, 'core/index.html')

<<<<<<< HEAD
def user_logout(request):
    logout(request)
    messages.success(request, '✔️Sesión Cerrada con ÉXITO')
    return render(request, 'core/index.html')

def listado_libros(request):
    # libros = [
    #     {
    #         'imagen': 'core/images/Cien Años de Soledad - Gabriel García Márquez.webp',
    #         'nombre': 'Cien Años de Soledad ',
    #         'autor': 'Gabriel García Márquez',
    #         'precio': '1.000'
    #     },
    #     {
    #         'imagen': 'core/images/Cincuenta Sombras de Grey - E. L. James.webp',
    #         'nombre': 'Cincuenta Sombras de Grey',
    #         'autor': 'E. L. James',
    #         'precio': '2.000'
    #     },
    #     {
    #         'imagen': 'core/images/Diario de Ana Frank - Ana Frank.webp',
    #         'nombre': 'Diario de Ana Frank',
    #         'autor': 'Ana Frank',
    #         'precio': '3.000'
    #     },
    #     {
    #         'imagen': 'core/images/Don Quijote de la Mancha - Miguel de Cervantes.webp',
    #         'nombre': 'Don Quijote de la Mancha',
    #         'autor': 'Miguel de Cervantes',
    #         'precio': '4.000'
    #     },
    #     {
    #         'imagen': 'core/images/El Código Da Vinci - Dan Brown.webp',
    #         'nombre': 'El Código Da Vinci',
    #         'autor': 'Dan Brown',
    #         'precio': '5.000'
    #     },
    #     {
    #         'imagen': 'core/images/El Principito - Antoine de Saint-Exupéry.webp',
    #         'nombre': 'El Principito',
    #         'autor': 'Antoine de Saint-Exupéry',
    #         'precio': '6.000'
    #     },
    #     {
    #         'imagen': 'core/images/El Psicoanalista - John Katzenbach.webp',
    #         'nombre': 'El Psicoanalista',
    #         'autor': 'John Katzenbach',
    #         'precio': '7.000'
    #     },
    #     {
    #         'imagen': 'core/images/Harry Potter y la Piedra Filosofal - J. K. Rowling.webp',
    #         'nombre': 'Harry Potter y la Piedra Filosofal',
    #         'autor': 'J. K. Rowling',
    #         'precio': '8.000'
    #     },
    #     {
    #         'imagen': 'core/images/Rayuela - Julio Cortázar.webp',
    #         'nombre': 'Rayuela',
    #         'autor': 'Julio Cortázar',
    #         'precio': '9.000'
    #     },
    #     {
    #         'imagen': 'core/images/Romeo y Julieta - William Shakespeare.webp',
    #         'nombre': 'Romeo y Julieta',
    #         'autor': 'William Shakespeare',
    #         'precio': '10.000'
    #     }
    # ]
    # books_sorted = sorted(libros, key=lambda x: x['nombre'])

=======
def listado_libros(request):
    # libros = [
    #     {
    #         'imagen': 'core/images/Cien Años de Soledad - Gabriel García Márquez.webp',
    #         'nombre': 'Cien Años de Soledad ',
    #         'autor': 'Gabriel García Márquez',
    #         'precio': '1.000'
    #     },
    #     {
    #         'imagen': 'core/images/Cincuenta Sombras de Grey - E. L. James.webp',
    #         'nombre': 'Cincuenta Sombras de Grey',
    #         'autor': 'E. L. James',
    #         'precio': '2.000'
    #     },
    #     {
    #         'imagen': 'core/images/Diario de Ana Frank - Ana Frank.webp',
    #         'nombre': 'Diario de Ana Frank',
    #         'autor': 'Ana Frank',
    #         'precio': '3.000'
    #     },
    #     {
    #         'imagen': 'core/images/Don Quijote de la Mancha - Miguel de Cervantes.webp',
    #         'nombre': 'Don Quijote de la Mancha',
    #         'autor': 'Miguel de Cervantes',
    #         'precio': '4.000'
    #     },
    #     {
    #         'imagen': 'core/images/El Código Da Vinci - Dan Brown.webp',
    #         'nombre': 'El Código Da Vinci',
    #         'autor': 'Dan Brown',
    #         'precio': '5.000'
    #     },
    #     {
    #         'imagen': 'core/images/El Principito - Antoine de Saint-Exupéry.webp',
    #         'nombre': 'El Principito',
    #         'autor': 'Antoine de Saint-Exupéry',
    #         'precio': '6.000'
    #     },
    #     {
    #         'imagen': 'core/images/El Psicoanalista - John Katzenbach.webp',
    #         'nombre': 'El Psicoanalista',
    #         'autor': 'John Katzenbach',
    #         'precio': '7.000'
    #     },
    #     {
    #         'imagen': 'core/images/Harry Potter y la Piedra Filosofal - J. K. Rowling.webp',
    #         'nombre': 'Harry Potter y la Piedra Filosofal',
    #         'autor': 'J. K. Rowling',
    #         'precio': '8.000'
    #     },
    #     {
    #         'imagen': 'core/images/Rayuela - Julio Cortázar.webp',
    #         'nombre': 'Rayuela',
    #         'autor': 'Julio Cortázar',
    #         'precio': '9.000'
    #     },
    #     {
    #         'imagen': 'core/images/Romeo y Julieta - William Shakespeare.webp',
    #         'nombre': 'Romeo y Julieta',
    #         'autor': 'William Shakespeare',
    #         'precio': '10.000'
    #     }
    # ]
    # books_sorted = sorted(libros, key=lambda x: x['nombre'])

>>>>>>> 160abb9fe1466c2f9be5777c6ddafefea10af58b
    # contexto = {
    #     'libros': books_sorted,
    # }
    libros = Libro.objects.all().order_by('id')
    contexto = {
        'libros': libros,
    }
    return render(request, 'core/listado_libros.html', contexto)

def crear_libro(request):
    contexto = {}
    if request.method == "GET":
        contexto['crear_libro_form'] = CrearLibroForm()
    else:
        form = CrearLibroForm(request.POST)
        contexto['crear_libro_form'] =  form
        if  form.is_valid(): 
            nuevo_libro = Libro(
                ISBN = form.cleaned_data['ISBN'],
                titulo = form.cleaned_data['titulo'],
                autor = form.cleaned_data['autor'],
                precio = form.cleaned_data['precio']
            )
            nuevo_libro.save()
            messages.success(request, '✔️El Libro fue creado con ÉXITO')
            return redirect('listado_libros')
    return render(request, 'core/crear_libro.html', contexto)

def modificar_libro(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)  # Retrieve the book to be modified
    if request.method == "GET":
        contexto = {'modificar_libro_form': ModificarLibroModelForm(instance=libro)}
        return render(request, 'core/modificar_libro.html', contexto)
    else:  # Se asume que es un POST
        form = ModificarLibroModelForm(request.POST, instance=libro)
        contexto = {'modificar_libro_form': form}
        if form.is_valid():
            form.save()
            messages.success(request, '✔️El Libro fue modificado con ÉXITO')
<<<<<<< HEAD
            return redirect('listado_libros')  # Or redirect to a specific list view
=======
            return redirect('libros')  # Or redirect to a specific list view
>>>>>>> 160abb9fe1466c2f9be5777c6ddafefea10af58b
    return render(request, 'core/modificar_libro.html', contexto)

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        libro.delete()
        messages.success(request, '✔️El Libro fue eliminado con ÉXITO')
<<<<<<< HEAD
        return redirect('listado_libros')
=======
        return redirect('libros')
>>>>>>> 160abb9fe1466c2f9be5777c6ddafefea10af58b
    contexto = {'libro': libro}
    return render(request, 'core/eliminar_libro.html', contexto)



class ClientesListView(ListView):
    model = Cliente
    context_object_name='Clientes'
    template_name='core/listado_clientes.html'
<<<<<<< HEAD
    ordering=['id']
=======
    ordering=['dni']
>>>>>>> 160abb9fe1466c2f9be5777c6ddafefea10af58b

def crear_cliente(request):
    contexto = {}
    if request.method == "GET":
        contexto['crear_cliente_form'] = CrearClienteForm()
    else:
        form = CrearClienteForm(request.POST)
        contexto['crear_cliente_form'] =  form
        if  form.is_valid(): 
            nuevo_cliente = Cliente(
                dni = form.cleaned_data['dni'],
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                email = form.cleaned_data['email']
            )
            nuevo_cliente.save()
            messages.success(request, '✔️El Cliente fue creado con ÉXITO')
            return redirect('listado_clientes')
    return render(request, 'core/crear_cliente.html', contexto)

def modificar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)  # Retrieve the book to be modified
    if request.method == "GET":
        contexto = {'modificar_cliente_form': ModificarClienteModelForm(instance=cliente)}
        return render(request, 'core/modificar_cliente.html', contexto)
    else:  # Se asume que es un POST
        form = ModificarClienteModelForm(request.POST, instance=cliente)
        contexto = {'modificar_cliente_form': form}
        if form.is_valid():
            form.save()
            messages.success(request, '✔️El Cliente fue modificado con ÉXITO')
            return redirect('listado_clientes')  # Or redirect to a specific list view
    return render(request, 'core/modificar_cliente.html', contexto)

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        cliente.delete()
        messages.success(request, '✔️El Cliente fue eliminado con ÉXITO')
        return redirect('listado_clientes')
    contexto = {'cliente': cliente}
    return render(request, 'core/eliminar_cliente.html', contexto)

class PedidosListView(ListView):
    model = Pedido
    context_object_name='Pedido'
    template_name='core/listado_pedidos.html'
    ordering=['id']
<<<<<<< HEAD
=======

def crear_pedido(request):
    contexto = {}
    if request.method == "GET":
        contexto['crear_pedido_form'] = CrearPedidoForm()
    else:
        form = CrearPedidoForm(request.POST)
        contexto['crear_pedido_form'] =  form
        if  form.is_valid(): 
            nuevo_pedido = Pedido(
                pedido = form.cleaned_data['pedido'],
                cliente = form.cleaned_data['cliente'],
                libro = form.cleaned_data['libro'],
                fechaPedido= form.cleaned_data['fechaPedido'],
                cantidad = form.cleaned_data['cantidad']
            )
            nuevo_pedido.save()
            messages.success(request, '✔️El Pedido fue creado con ÉXITO')
            return redirect('listado_pedidos')
    return render(request, 'core/crear_pedido.html', contexto)
>>>>>>> 160abb9fe1466c2f9be5777c6ddafefea10af58b
