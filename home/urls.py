from django.urls import path
from .views import index, CustomPasswordResetView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
