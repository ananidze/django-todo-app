from django.urls import path

from todo.views import home, delete, incomplete, complete

urlpatterns = [
    path('', home, name='home'),
    path('delete/<str:id>', delete, name='Delete'),
    path('incomplete/<str:id>', incomplete, name='incomplete'),
    path('complete/<str:id>', complete, name='complete')
]