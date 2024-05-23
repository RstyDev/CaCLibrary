from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Libro
from .forms import *

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
    return render(request, 'core/index.html')

def libros(request):
    libros = [
        {
            'imagen': 'core/images/Cien Años de Soledad - Gabriel García Márquez.webp',
            'nombre': 'Cien Años de Soledad ',
            'autor': 'Gabriel García Márquez',
            'precio': '1.000'
        },
        {
            'imagen': 'core/images/Cincuenta Sombras de Grey - E. L. James.webp',
            'nombre': 'Cincuenta Sombras de Grey',
            'autor': 'E. L. James',
            'precio': '2.000'
        },
        {
            'imagen': 'core/images/Diario de Ana Frank - Ana Frank.webp',
            'nombre': 'Diario de Ana Frank',
            'autor': 'Ana Frank',
            'precio': '3.000'
        },
        {
            'imagen': 'core/images/Don Quijote de la Mancha - Miguel de Cervantes.webp',
            'nombre': 'Don Quijote de la Mancha',
            'autor': 'Miguel de Cervantes',
            'precio': '4.000'
        },
        {
            'imagen': 'core/images/El Código Da Vinci - Dan Brown.webp',
            'nombre': 'El Código Da Vinci',
            'autor': 'Dan Brown',
            'precio': '5.000'
        },
        {
            'imagen': 'core/images/El Principito - Antoine de Saint-Exupéry.webp',
            'nombre': 'El Principito',
            'autor': 'Antoine de Saint-Exupéry',
            'precio': '6.000'
        },
        {
            'imagen': 'core/images/El Psicoanalista - John Katzenbach.webp',
            'nombre': 'El Psicoanalista',
            'autor': 'John Katzenbach',
            'precio': '7.000'
        },
        {
            'imagen': 'core/images/Harry Potter y la Piedra Filosofal - J. K. Rowling.webp',
            'nombre': 'Harry Potter y la Piedra Filosofal',
            'autor': 'J. K. Rowling',
            'precio': '8.000'
        },
        {
            'imagen': 'core/images/Rayuela - Julio Cortázar.webp',
            'nombre': 'Rayuela',
            'autor': 'Julio Cortázar',
            'precio': '9.000'
        },
        {
            'imagen': 'core/images/Romeo y Julieta - William Shakespeare.webp',
            'nombre': 'Romeo y Julieta',
            'autor': 'William Shakespeare',
            'precio': '10.000'
        }
    ]
    books_sorted = sorted(libros, key=lambda x: x['nombre'])

    contexto = {
        'libros': books_sorted,
    }
    return render(request, 'core/libros.html', contexto)

def contacto(request):

    contexto = {}

    if request.method == "GET":
        contexto['contato_forms'] = contactoForm()
    else: #Se asume que es un POST
        form = contactoForm(request.POST)
        contexto['contato_forms'] = form

        if form.is_valid(): 
            messages.success(request, '✔️Tu Mensaje fue Enviado con ÉXITO')
            return redirect('index')

    return render(request, 'core/contacto.html', contexto)
