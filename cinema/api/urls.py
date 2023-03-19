from django.urls import path
from . import views

urlpatterns = [
    path('', views.LCFilmView.as_view()),
    path('<int:pk>/', views.RUDFilmView.as_view()),
    path('genre/', views.LCGenreView.as_view()),
    path('genre/<int:pk>/', views.RUDGenreView.as_view()),
    path('director/', views.LCDirectorView.as_view()),
    path('director/<int:pk>/', views.RUDDirectorView.as_view()),
    path('poster/', views.LCPosterView.as_view()),
    path('poster/<int:pk>/', views.RUDPosterView.as_view()),
]