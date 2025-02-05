from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar-conta/', views.criar_conta, name='criar_conta'),
    path('login/', views.login_view, name='login'),
    path('categoria/<int:categoria_id>/', views.categoria_produtos, name='categoria_produtos'),
]
