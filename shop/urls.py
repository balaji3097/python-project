from django.urls import path
from . import views

urlpatterns =[
    path('',views.garments,name='garments'),
    path('search',views.search,name='search')
    


]