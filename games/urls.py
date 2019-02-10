from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('add/', views.add_game, name='add'),
    path('<int:pk>/', views.GameView.as_view(), name='detail')
]
