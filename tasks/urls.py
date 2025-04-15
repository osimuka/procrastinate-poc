from django.urls import path
from . import views

urlpatterns = [
    path("tasks/add/", views.trigger_add_task, name="trigger_add_task"),
]
