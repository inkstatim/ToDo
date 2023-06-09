from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import Task
from .forms import TaskFrom
from django.shortcuts import redirect
from django.db.models import Q


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )
        return queryset


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


class TaskToggleCompleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.completed = not task.completed
        task.save()
        return redirect('todo:task_list')
# Create your views here.
