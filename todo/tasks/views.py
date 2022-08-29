from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.urls import reverse_lazy
from .models import Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['name']
    template_name = 'new_task.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks.html'

class TaskListUserView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks.html'

    def get_queryset(self):
        return Task.objects.filter(user__id=self.kwargs['user_id'])

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'detail_task.html'


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name']
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'task_confirm_delete.html'



