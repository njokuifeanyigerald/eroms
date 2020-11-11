"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from hello.views import index
from hello.views import indexs
from hello.views import delete_view
from hello.views import edit_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app2/', index, name = 'add'),
    path('app1/', indexs, name = 'home'),    
    path('app2/delete/<id>', delete_view, name = 'remove' ),
    path('app2/edit/<id>', edit_view, name = 'edited' ),
    path('', indexs),


    
]
