
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Survey, SurveyAnswer, QuestionAnswer, Choice, Question

def index(request):
    ctx = {}
    return render(request, 'main.html', ctx)

def admin_login(request):
    admin_username = request.POST['username']
    admin_password = request.POST['password']
    user = authenticate(request, username = admin_username, password = admin_password)
    if user is not None:
        login(request, user)
        return redirect('admin-panel')
    ctx = {'message':"Unable to login as administrator"}
    return render(request, 'error.html', ctx)


def admin_panel(request):
    surveys = Survey.objects.all()
    ctx = {'surveys': surveys}
    return render(request,'admin-dashboard.html',ctx)


def admin_answers(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    answers = survey.surveyanswer_set.all()
    ctx = {'survey':survey, 'answers':answers}
    return render(request,'admin-survey-detail.html',ctx)


def survey_create_view(request):
    return render(request,'survey-create.html',{})


def question_add_view(request):
    return render(request,'question-add.html',{})


def choice_add_view(request):
    question = Question.objects.get(id=int(request.session['current_question']))
    return render(request,'choice-add.html',{'question':question})


def survey_create(request):
    newSurvey = Survey()
    newSurvey.title = request.POST['survey_title']
    newSurvey.save()
    request.session['current_survey'] = newSurvey.id
    return redirect('admin-question-add-view')


def question_add(request):
    survey_add = Survey.objects.get(id=int(request.session['current_survey']))
    newQuestion = Question()
    newQuestion.question_text = request.POST['question_text']
    newQuestion.survey = survey_add
    newQuestion.save()
    survey_add.question_set.add(newQuestion)
    survey_add.save()
    request.session['current_question'] = newQuestion.id
    return redirect('admin-choice-add-view')


def choice_add(request):
    question = Question.objects.get(id = int(request.session['current_question']))
    newChoice = Choice()
    newChoice.choice_text = request.POST['choice_text']
    newChoice.question = question
    newChoice.save()
    question.choice_set.add(newChoice)
    question.save()
    return redirect('admin-choice-add-view')


def survey_delete(request):
    survey_deletion = request.POST['sv_delete']
    sv_del = Survey.objects.get(id=int(survey_deletion))
    sv_del.delete()
    return redirect('admin-panel')


def survey_view(request, survey_id = None):
    try:
        survey = Survey.objects.get(id = survey_id)
        questions = survey.question_set.all()
        ctx = {
           'survey':survey,
           'questions':questions,
          }
    except:
        error_message = "Survey #" + str(survey_id) + " not found"
        return render(request,'error.html',{'message':error_message})
    return render(request,'survey-view.html',ctx)


def load_survey(request):
    survey_id = request.POST['survey_id']
    return redirect('survey-view', int(survey_id))


def survey_fill(request):
    answer = SurveyAnswer()
    survey_submitted = Survey.objects.get(id=request.POST['survey_id'])
    answer.survey = survey_submitted
    answer.save()

    questions = survey_submitted.question_set.all()

    for question in questions:
        question_post = request.POST['question'+str(question.id)]
        qa = QuestionAnswer()
        qa.survey_answer = answer
        qa.choice = Choice.objects.get(id=int(question_post))
        qa.save()

    return render(request,'survey-complete.html',{})
