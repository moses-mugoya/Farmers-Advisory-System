from django.shortcuts import render
from .forms import DiagnoseForm, QuestionForm, MailForm, PlantsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Diagnose, Common
from django.core.mail import send_mail
from django.contrib.auth.models import User


def index(request):
    commons = Common.objects.all()
    return render(request, 'diagnose/index.html', {'commons': commons})


@login_required
def diagnose(request):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    display1 = Diagnose.objects.get(name='Foot and Mouth')
    display2 = Diagnose.objects.get(name='Brucellosis')
    display3 = Diagnose.objects.get(name='Bovine Tubercluosis')
    display4 = Diagnose.objects.get(name='Bracken Poisoning')
    display5 = Diagnose.objects.get(name='Anaemia – Theileria')
    max_value = 0
    display = []
    values = []
    if request.method == 'POST':
        form = DiagnoseForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['category1'] == 'sor':
                var1 = var1 + 1
            if form.cleaned_data['category1'] == 'dre':
                var2 = var2 + 1
            if form.cleaned_data['category1'] == 'ema':
                var3 = var3 + 1
            if form.cleaned_data['category1'] == 'blood':
                var4 = var4 + 1
            if form.cleaned_data['category1'] == 'let':
                var5 = var5 + 1

            if form.cleaned_data['category2'] == 'pain':
                var1 = var1 + 1
            if form.cleaned_data['category2'] == 'weak':
                var3 = var3 + 1
            if form.cleaned_data['category2'] == 'joint':
                var2 = var2 + 1
            if form.cleaned_data['category2'] == 'Fatigue':
                var4 = var4 + 1

            if form.cleaned_data['category3'] == 'Irritability':
                var1 = var1 + 1
            if form.cleaned_data['category3'] == 'Loss':
                var2 = var2 + 1
            if form.cleaned_data['category3'] == 'Anorexia':
                var3 = var3 + 1
            if form.cleaned_data['category3'] == 'abd':
                var4 = var4 + 1
            if form.cleaned_data['category3'] == 'int':
                var5 = var5 + 1

            if form.cleaned_data['category4'] == 'Backache':
                var2 = var2 + 1
            if form.cleaned_data['category4'] == 'fever':
                var1 = var1 + 1
            if form.cleaned_data['category4'] == 'moist':
                var3 = var3 + 1
            if form.cleaned_data['category4'] == 'panting':
                var4 = var4 + 1

            if form.cleaned_data['category5'] == 'red Rash':
                var1 = var1 + 1
            if form.cleaned_data['category5'] == 'chills':
                var2 = var2 + 1

            values.append(var1)
            values.append(var2)
            values.append(var3)
            values.append(var4)
            values.append(var5)

            for var in values:
                print(var)

            max_value = max(values)
            if max_value == var1:
                display.append(display1)
            elif max_value == var2:
                display.append(display2)
            elif max_value == var3:
                display.append(display3)
            elif max_value == var4:
                display.append(display4)
            elif max_value == var5:
                display.append(display5)
    else:
        form = DiagnoseForm()
    return render(request, 'diagnose/diagnose.html', {'form': form, 'display': display})


@login_required
def plant_diagnose(request):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    display1 = Diagnose.objects.get(name='Aphids')
    display2 = Diagnose.objects.get(name='Cucumber Mosaic Virus')
    display3 = Diagnose.objects.get(name='Rhizoctonia')
    display4 = Diagnose.objects.get(name='Mealybugs')
    max_value = 0
    display = []
    values = []
    if request.method == 'POST':
        form = PlantsForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['category1'] == 'bla':
                var1 = var1 + 1
            if form.cleaned_data['category1'] == 'sho':
                var2 = var2 + 1
            if form.cleaned_data['category1'] == 'for':
                var3 = var3 + 1
            if form.cleaned_data['category1'] == 'def':
                var4 = var4 + 1

            if form.cleaned_data['category2'] == 'cri':
                var2 = var2 + 1
            if form.cleaned_data['category2'] == 'wil':
                var1 = var1 + 1
            if form.cleaned_data['category2'] == 'sun':
                var3 = var3 + 1
            if form.cleaned_data['category2'] == 'stunt':
                var4 = var4 + 1

            if form.cleaned_data['category3'] == 'dry':
                var3 = var3 + 1
            if form.cleaned_data['category3'] == 'yel':
                var1 = var1 + 1
            if form.cleaned_data['category3'] == 'lea':
                var2 = var2 + 1
            if form.cleaned_data['category3'] == 'mea':
                var4 = var4 + 1

            if form.cleaned_data['category4'] == 'col':
                var1 = var1 + 1
            if form.cleaned_data['category4'] == 'stu':
                var2 = var2 + 1
            if form.cleaned_data['category4'] == 'dyi':
                var4 = var4 + 1
            if form.cleaned_data['category4'] == 'ste':
                var3 = var3 + 1

            if form.cleaned_data['category5'] == 'nut':
                var3 = var3 + 1
            if form.cleaned_data['category5'] == 'hon':
                var1 = var1 + 1
            if form.cleaned_data['category5'] == 'you':
                var2 = var2 + 1
            if form.cleaned_data['category5'] == 'chl':
                var4 = var4 + 1

            values.append(var1)
            values.append(var2)
            values.append(var3)
            values.append(var4)

            for var in values:
                print(var)

            max_value = max(values)
            if max_value == var1:
                display.append(display1)
            elif max_value == var2:
                display.append(display2)
            elif max_value == var3:
                display.append(display3)
            elif max_value == var4:
                display.append(display4)
    else:
        form = PlantsForm()
    return render(request, 'diagnose/plant.html', {'form': form, 'display': display})


@login_required
def question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Your question has been received successfully')
    else:
        form = QuestionForm()
    return render(request, 'diagnose/question.html', {'form': form})


def send_email(request):
    users = User.objects.all()
    if request.method == 'POST':
        mail_form = MailForm(data=request.POST)
        if mail_form.is_valid():
            for user in users:
                subject = mail_form.cleaned_data['subject']
                message = mail_form.cleaned_data['body']
                sender = 'admin@gmail.com'
                receiver = user.email
                send_mail(subject, message, sender, [receiver], fail_silently=False,)
            new_mail = mail_form.save(commit=False)
            new_mail.user = request.user
            new_mail.save()
            messages.success(request, 'Email sent successfully')
        else:
            messages.error(request, 'Error sending the email!')
    else:
        mail_form = MailForm()
    return render(request, 'diagnose/admin.html', {'mail_form': mail_form})
