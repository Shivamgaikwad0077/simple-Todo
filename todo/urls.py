from django.urls import path
from . import views

urlpatterns = [
    #add task
    path('addTask/', views.addTask, name="addTask"),
    # Marks as done
    path('mark_as_done/<int:pk>/', views.mark_as_done , name='mark_as_done'),
    # Marks as Undone
    path('mark_as_undone/<int:pk>/', views.marks_as_undone , name='mark_as_undone'),

    # Edit Features
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),

    #Delete Task
    path('delete_task/<int:pk>', views.delete_task, name='delete_task')
]