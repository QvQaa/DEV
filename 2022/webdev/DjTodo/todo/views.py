from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin
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


class TodoMOMCV(MultipleObjectMixin, CreateView):  # 상속 받는 순서도 중요함.
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form_list.html'
    success_url = reverse_lazy('todo:mixin')

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        # 앞에있는 인자에서 get query set(여기서는 MultipleObjectMixin)
        return super().get(request, *args, **kwargs)  # 인자는 동일하게 써주는게 보통임

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)


class TodoDelV2(DeleteView):
    model = Todo
    #template_name = 'todo/todo_confirm_delete.html'
    # 아직 urls.py 모듈이 로딩이 안된상태 항상 reverse_lazy 사용
    success_url = reverse_lazy('todo:mixin')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def Test(request):
    return render(request, 'todo/test.html')
