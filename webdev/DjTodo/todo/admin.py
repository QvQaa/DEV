from django.contrib import admin

from todo.models import Todo, DateTest


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo')
