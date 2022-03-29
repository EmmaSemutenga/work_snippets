from django import forms
from .models import Question

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    pub_date = forms.DateTimeField(label_suffix="yyyy-mm-dd hh:mm:ss")

class AnswerForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    choice_text = forms.CharField(max_length=200)

class VoteForm(forms.Form):
    # pas = forms.ModelChoiceIterator()
    # still figuring out how to get choices for this particular question into the radio
    pass
