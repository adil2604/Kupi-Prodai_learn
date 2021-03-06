"""KupiProdai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('ad/<int:pk>/', views.ad_detail,name='ad_detail'),
    path('cart/',include('cart.urls',namespace='cart')),
    path('login', views.login_view,name='login'),
    path('register',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('product_list/',views.product_list_view,name='product_list'),
    path('product_add',views.product_add_view),
    path('new',views.new_view),
    path('',views.main_page)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)