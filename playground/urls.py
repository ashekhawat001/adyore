from django.urls import path
from . import views

urlpatterns=[

    path('fucker/', views.say_hello)
]