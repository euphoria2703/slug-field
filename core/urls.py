from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home),
    path('<slug:slug>/', detail, name = 'detail')
]