from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import DateTest
#from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    date = get_object_or_404(DateTest)
    context = {'date_list': date}
    return render(request, 'date:date_home', context)
