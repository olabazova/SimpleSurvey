from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=100)


class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    survey = models.ForeignKey(Survey, on_delete = models.CASCADE)


class Choice(models.Model):
    choice_text = models.CharField(max_length=1000)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)


class SurveyAnswer(models.Model):
    survey = models.ForeignKey(Survey, on_delete = models.CASCADE)


class QuestionAnswer(models.Model):
    survey_answer = models.ForeignKey(SurveyAnswer, on_delete = models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE)
