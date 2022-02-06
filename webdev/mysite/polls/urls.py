from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'polls'
urlpatterns = [
    # ex : /polls/
    path('', views.index, name='index'),
    # ex : /polls/5/
    path('<int:question_id>/', views.detail,  # django에서 지원하는 url pattern
         name='detail'),                     # question_id 는 view의 question_id와 일치
    # ex : /polls/5/results/
    path('<int:question_id>/results/', views.result,
         name='results'),
    # ex : /polls/5/vote/
    path('<int:question_id>/vote/', views.vote,
         name='vote'),
]
