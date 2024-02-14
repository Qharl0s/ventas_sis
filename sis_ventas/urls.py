from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView,PasswordChangeView, PasswordResetDoneView)
from aplicacion.views import inicio, caja, venta, mostrador, almacen, perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('', inicio, name='inicio'),
    path('caja/', caja, name='caja'),
    path('venta/', venta, name='venta'),
    path('mostrador/', mostrador, name='mostrador'),
    path('almacen/', almacen, name='almacen'),
    path('perfil/', perfil, name='perfil'),

]
