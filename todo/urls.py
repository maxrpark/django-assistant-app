from django.urls import path

from .views import HomeView, TodoView, EditView, DeleteView, CompleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('todo', TodoView.as_view(), name='todo'),
    path('delete/<int:id>', DeleteView.as_view(), name='delete', ),
    path('todo/edit/<int:id>', EditView.as_view(), name='todo-edit'),
    path('todo/complete/<int:id>', CompleteView.as_view(), name='complete'),
]
