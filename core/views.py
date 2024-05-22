from django.shortcuts import render
from django.http import HttpResponse
from models import Libro

# Create your views here.
def index(request):
    return HttpResponse('HolaMundo')

def ventas(request):
    libros=[Libro("Python Crash Course: A Hands-On, Project-Based Introduction to Programming","Eric Matthes","Programación","No Starch Press",2019),
            Libro("Automate the Boring Stuff with Python: Practical Programming for Total Beginners","Al Sweigart","Programación","No Starch Press",2019),
            Libro("Fluent Python: Clear, Concise, and Effective Programming","Luciano Ramalho","Programación","O'Reilly Media",2015),
            Libro("Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython","Wes McKinney","Ciencia de Datos","O'Reilly Media",2017),
            Libro("Effective Python: 90 Specific Ways to Write Better Python","Brett Slatkin","Programación","Addison-Wesley Professional",2015)]
    context = { "libros":libros }
    return render(request, "core/pages/get_libros.html",context)