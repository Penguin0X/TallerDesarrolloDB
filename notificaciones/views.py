from django.views.generic import ListView, CreateView, UpdateView
from .models import Notification
from .forms import NotificationForm

class NotificacionListView(ListView):
    model = Notification
    template_name = 'notificaciones/notification_list.html'
    context_object_name = 'notifications'

class NotificacionCreateView(CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notificaciones/notification_form.html'
    success_url = '/notificaciones/'  # Asegúrate de que la URL de éxito esté correctamente configurada

class NotificacionUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notificaciones/notification_form.html'
    success_url = '/notificaciones/'  # Asegúrate de que la URL de éxito esté correctamente configurada
