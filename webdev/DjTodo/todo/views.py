from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from todo.models import Todo, DateTest


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'


class TodoCV(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list')


class TodoLV(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'


class TodoDelV(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    # 아직 urls.py 모듈이 로딩이 안된상태 항상 reverse_lazy 사용
    success_url = reverse_lazy('todo:list')


def DateV(request):
    date_list = get_object_or_404(DateTest)
    context = {'date_list': date_list}
    return render(request, 'todo/todo_date_test.html', context)
    # return render(request, 'todo/todo_date_test.html')
