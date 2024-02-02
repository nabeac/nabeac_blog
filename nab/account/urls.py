from django.urls import path
from .views import createuser
urlpatterns = [
    path('', createuser, name='createuser')
]