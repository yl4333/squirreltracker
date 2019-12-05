from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/add', views.add, name='add'),
    # path('<str:squirrel_id>/', views.update, name='update'),
]