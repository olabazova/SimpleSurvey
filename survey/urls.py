
from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name="root"),
    path('admin_login/', views.admin_login, name="admin-login"),
    path('admin_dashboard/', views.admin_panel, name="admin-panel"),
    path('admin_dashboard/survey_delete/',views.survey_delete,name="admin-survey-delete"),
    path('admin_dashboard/survey/<int:survey_id>/',views.admin_answers,name="answer-detail"),
    path('admin-dashboard/survey_create_view', views.survey_create_view, name="admin-survey-create-view"),
    path('admin-dashboard/survey_create/', views.survey_create, name="admin-survey-create"),
    path('admin-dashboard/question_add_view/', views.question_add_view, name="admin-question-add-view"),
    path('admin-dashboard/question_add/', views.question_add, name="admin-question-add"),
    path('admin-dashboard/choice_add_view/', views.choice_add_view, name="admin-choice-add-view"),
    path('admin-dashboard/choice_add/', views.choice_add, name="admin-choice-add"),

    path('survey_load/<int:survey_id>/', views.survey_view, name="survey-view"),
    path('survey_load/',views.load_survey, name="load-survey"),
    path('fill-survey',views.survey_fill,name="fill-survey"),
]
