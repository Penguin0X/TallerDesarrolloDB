from django.urls import path
from .views import JuegoListView, JuegoCreateView, JuegoEditView, JuegoDeleteView, StockUpdateView, agregar_juego, listar_juegos

urlpatterns = [
    path('', JuegoListView.as_view(), name='juego_list'),
    path('juegos/', JuegoListView.as_view(), name='juego_list'),
    path('juegos/create/', JuegoCreateView.as_view(), name='juego_create'),
    path('juegos/<int:pk>/edit/', JuegoEditView.as_view(), name='juego_edit'),
    path('agregar_juego/', agregar_juego, name='agregar_juego'),
    path('listar_juegos/', listar_juegos, name='listar_juegos'),
    path('editar_juego/<int:pk>/', JuegoEditView.as_view(), name='juego_edit'),
    path('borrar_juego/<int:pk>/', JuegoDeleteView.as_view(), name='juego_delete'),
    path('gestionar_stock/<int:pk>/', StockUpdateView.as_view(), name='gestionar_stock'),
]
