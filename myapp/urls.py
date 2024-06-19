# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('render_task_item/', views.render_task_item, name='render_task_item'),
]
