from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task


# class TaskDetail(DetailView):
#     model = Task


# class TaskCreate(CreateView):
#     model = Task
#     fields = ['title', 'description', 'complete']
#     success_url = reverse_lazy('tasks')


# class TaskUpdate(UpdateView):
#     model = Task
#     fields = ['title', 'description', 'complete']
#     success_url = reverse_lazy('tasks')


# class TaskDelete(DeleteView):
#     model = Task
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks')
