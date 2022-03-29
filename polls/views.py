from django.shortcuts import redirect, render, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question, Choice
from selenium import webdriver
import os
from django.views import generic
from django.utils import timezone


# os.environ['PATH'] += '/home/emmanuel/mysite/chromedriver' #for chrome driver
# os.environ['PATH'] += '/home/emmanuel/mysite/geckodriver' #for firefox driver

# Create your views here.
# def home(request):
#     driver = webdriver.Firefox()
#     driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
#     driver.implicitly_wait(3)
#     element = driver.find_element_by_id('downloadButton')
#     element.click()
#     # print(driver)
#     return render(request, 'home.html')

# def questions_list(request):
#     questions = Question.objects.all()
#     return render(request, 'polls/questions.html', {'questions':questions})
class IndexView(generic.ListView):
    template_name = 'polls/questions.html'
    context_object_name = 'questions'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choices__isnull=True).order_by('-pub_date')[:5]


# def vote_me(request, id):
#     question = get_object_or_404(Question, pk=id)
#     if request.method == 'POST':
#         choice_selected = question.choices.get(id=request.POST['choice'])
#         choice_selected.votes +=1
#         choice_selected.save()
#         return redirect('polls:questions')

# def question_detail(request, id):
#     question = get_object_or_404(Question, pk=id)
#     return render(request, 'polls/question_detail.html', {'question':question})

class DetailView(generic.DetailView):
    template_name = 'polls/question_detail.html'
    context_object_name = 'question'
    model = Question

    # method below will generate the queryset where the single object will be searched using the pk
    # What we have works well; however, even though future questions don’t appear in the questions view, users can still reach them
    # if they know or guess the right URL. So we need to add a similar constraint to DetailView:
    def get_queryset(self):
        """
        exclude any question with pubdate in the future and has no choices
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choices__isnull=True)
    
        

def add_question(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # print(request.POST.get('question_text'))
        # print(request.POST.get('pub_date'))
        if form.is_valid():
            Question.objects.create(question_text=form.cleaned_data.get('question_text'), pub_date=form.cleaned_data.get('pub_date'))
            return redirect('polls:questions')
    return render(request, 'polls/add_question.html', {'form':form})

def add_answer(request):
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(id=request.POST.get('question'))
            choice_text = form.cleaned_data.get('choice_text')
            Choice.objects.create(question = question, choice_text=choice_text)
            return redirect('polls:questions')
    return render(request, 'polls/add_answer.html', {'form':form})

def vote(request, id):
    question = Question.objects.get(id=id)
    if request.method == 'POST':
        choice = Choice.objects.get(id=request.POST.get('choice'))
        choice.votes += 1
        choice.save()
        return redirect('polls:question_detail', pk=question.id)
    return render(request, 'polls/question_detail.html', {'question':question})
