from django.urls import re_path
from . import views

app_name = 'diagnose'

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^animal/', views.diagnose, name='diagnose'),
    re_path('^plant/', views.plant_diagnose, name='plant'),
    re_path('^question/', views.question, name='question'),
    re_path('^email/', views.send_email, name='email'),

]

