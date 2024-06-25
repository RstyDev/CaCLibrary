from django.contrib.auth import views as auth_view
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='core/registration/login.html', redirect_field_name='index'), name='login'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('accounts/password_reset/', auth_view.PasswordResetView.as_view(template_name='core/registration/password_reset.html'), name='password_reset'),
    
    path('listado_libros', views.listado_libros, name='listado_libros'),
    path('crear_libro', views.crear_libro, name='crear_libro'),
    path('modificar_libro/<int:libro_id>/', views.modificar_libro, name='modificar_libro'),
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),

    path('listado_clientes', views.ClientesListView.as_view(), name='listado_clientes'),
    path('crear_cliente', views.crear_cliente, name='crear_cliente'),
    path('modificar_cliente/<int:cliente_id>/', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    
    path('listado_pedidos', views.PedidosListView.as_view(), name='listado_pedidos')
]