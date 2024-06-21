from django.urls import path, include
from . import routing  # Importa las rutas WebSocket de tu aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('render_task_item/', views.render_task_item, name='render_task_item'),
    path('ws/', include(routing.websocket_urlpatterns)),  # Rutas WebSocket de tu aplicación
]
