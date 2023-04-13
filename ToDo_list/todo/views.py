from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Task
from .forms import TaskFrom


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskFrom
    template_name = 'todo/task_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskFrom
    template_name = 'todo/task_update.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = '/'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'

# Create your views here.
