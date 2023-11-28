from django.urls import path
from .views import *

urlpatterns = [
    path('', categories, name='categories'),
    path('create-client/', create_client, name='create_client'),
    path('create-user/', create_user, name='create_user'),
    path('login/', auth, name='login'),
    path('response/', response_get, name='response'),
]