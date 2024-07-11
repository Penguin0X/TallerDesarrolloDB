from django.urls import path
from .views import NotificacionListView, NotificacionCreateView, NotificacionUpdateView

urlpatterns = [
    path('', NotificacionListView.as_view(), name='notification_list'),
    path('create/', NotificacionCreateView.as_view(), name='notification_create'),
    path('<int:pk>/edit/', NotificacionUpdateView.as_view(), name='notification_edit'),
]