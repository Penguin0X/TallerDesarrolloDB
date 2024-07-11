from django.urls import path
from .views import PersonalListView, PersonalCreateView, PersonalUpdateView

urlpatterns = [
    path('personal/', PersonalListView.as_view(), name='personal_list'),
    path('personal/create/', PersonalCreateView.as_view(), name='personal_create'),
    path('personal/<int:pk>/edit/', PersonalUpdateView.as_view(), name='personal_edit'),
]
