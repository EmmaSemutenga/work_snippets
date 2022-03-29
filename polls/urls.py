from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # path('', views.home, name='home'),
    path('add_question/', views.add_question, name="add_question"),
    path('add_answer/', views.add_answer, name="add_answer"),
    path('', views.IndexView.as_view(), name="questions"),
    path('question_detail/<int:pk>/', views.DetailView.as_view(), name="question_detail"),
    path('vote/<int:id>/', views.vote, name="vote"),
    # path('results/<int:pk>/', views.ResultsView.as_view(), name="results"),
]