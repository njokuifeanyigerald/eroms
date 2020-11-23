from django.urls import path
from .views import *

urlpatterns = [
    path('add/', index, name = 'add'),
    path('add/delete/<id>', delete_view, name = 'remove' ),
    path('add/edit/<id>', edit_view, name = 'edited' ),
    path('', indexs,name = 'home'),
    # path('bmi/',Bmi, name='Bmi'),
    # path('B/',Bmiview, name='bmiview'),

    
]
