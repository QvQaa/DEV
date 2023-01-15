from django.http import JsonResponse
from django.views.generic import ListView
from todo.models import Todo


class ApiTodoLV(ListView):
    model = Todo
    # template_name=

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())
        return JsonResponse(data=todoList, safe=False)
