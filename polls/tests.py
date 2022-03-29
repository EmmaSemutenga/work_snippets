from ast import arg
from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse
# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns false for questions with future pub date
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), True)

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no question exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('polls:questions'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls found")
        self.assertQuerysetEqual(response.context['questions'], [])

    def test_future_question(self):
        """
        Questions with a pub date in the future aren't displayed on the questions page
        """
        create_question("future question", 2)
        response = self.client.get(reverse('polls:questions'))
        self.assertContains(response, "No polls found")
        self.assertQuerysetEqual(response.context['questions'], [])

    def test_past_question(self):
        """
        Questions with a pub date in the past are displayed on the questions page
        """
        question = create_question("future question", -2)
        question.choices.create(choice_text="kiki naye")
        response = self.client.get(reverse('polls:questions'))
        self.assertQuerysetEqual(response.context['questions'], [question,])

    def test_future_question_and_past_question(self):
        """Even if both past and future questions exist, only past questions are displayed"""
        question1 = create_question("future question", 2)
        question1.choices.create(choice_text="kiki naye")
        question2 = create_question("future question", -2)
        question2.choices.create(choice_text="kiki naye")
        response = self.client.get(reverse('polls:questions'))
        self.assertQuerysetEqual(response.context['questions'], [question2,])

    def test_two_past_questions(self):
        """
        The questions page may display multiple questions
        """
        question1 = create_question("future question", -32)
        question1.choices.create(choice_text="kiki naye")
        question2 = create_question("future question", -2)
        question2.choices.create(choice_text="kiki naye")
        response = self.client.get(reverse('polls:questions'))
        self.assertQuerysetEqual(response.context['questions'], [question2,question1])

    def test_question_has_no_choices(self):
        """
        The questions page may display only questions with choices
        """
        question1 = create_question("Past question", -32)
        question1.choices.create(choice_text="Waridu")
        response = self.client.get(reverse('polls:questions'))
        self.assertQuerysetEqual(response.context['questions'], [question1,])

class QuestionDetailViewTests(TestCase):

    def test_past_question_displayed(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        question1 = create_question("Past question", -32)
        question1.choices.create(choice_text="Waridu")
        response = self.client.get(reverse('polls:question_detail', args=(question1.id, )))
        self.assertEqual(response.context['question'], question1)

    def test_future_question_not_displayed(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        question1 = create_question("Future question", 32)
        question1.choices.create(choice_text="Waridu")
        response = self.client.get(reverse('polls:question_detail', args=(question1.id, )))
        self.assertEqual(response.status_code, 404)