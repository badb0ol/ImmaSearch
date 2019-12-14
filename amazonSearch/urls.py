from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('', views.home, name='home')

    #path('start/', views.start, name='start'), format with start being the page to open
]
