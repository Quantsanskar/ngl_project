from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_question, name='submit_question'),
    path('questions/bdhjd/jndj/njf/', views.view_questions, name='view_questions'),
]
