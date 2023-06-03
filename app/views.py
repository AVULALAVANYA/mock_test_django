from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView



def registration(request):
    ufo=UserForm()
    d={'ufo':ufo}
    if request.method=='POST':
        ufd=UserForm(request.POST)
        if ufd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            send_mail('registration',
            'your registration is sucessful',
                     'arlavanya123@gmail.com',
                     [NSUFO.email],
                    fail_silently=False)
            
            return HttpResponse('Registered sucessfully')
        else:
            return HttpResponse('data is in valid')

    return render(request,'registration.html',d)
class QuestionList(ListView):
    model = Question
    context_object_name='questions'

class QuestionDetail(DetailView):
    model =Question
    context_object_name='Qcl' 

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username,'questions':questions}
        return render(request,'home.html',d)
    return render(request,'home.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AO=authenticate(username=username,password=password)
        if AO and AO.is_active:
            login(request,AO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid user data')
    return render(request,'user_login.html')

@login_required
def questions(request):
    qfo=QuestionForm()
    d={'qfo':qfo}
    if request.method=='POST':
        qfd=QuestionForm(request.POST)
        if qfd.is_valid():
            username=request.session['username']
            UO=User.objects.get(username=username)
            NSQO=qfd.save(commit=False)
            NSQO.user=UO
            NSQO.save()
            return HttpResponse(reverse('QuestionList'))
        else:
            return HttpResponse('not valid ')
    return render(request,'questions.html',d)

def display_questions(request):
    QO=Question.objects.all()
    d={'QO':QO}
    return render(request,'display_questios.html',d)

@login_required
def answer_question(request):
    aqo = AnswerForm()
    d={'aqo':aqo}
    question = Question.objects.all()
    if request.method == 'POST':
        aqd= AnswerForm(request.POST)
        if aqd.is_valid():
            username=request.session['username']
            UO=User.objects.get(username=username)
            NSAQO = aqd.save(commit=False)
            NSAQO.user = UO
            NSAQO.save()
            Q=NSAQO.question
            AO=Answer.objects.filter(question=Q)
            d1={'AO':AO}
            return HttpResponseRedirect(reverse('QuestionList'))
        else:
            return HttpResponse('quiestion not asked successfully')
        
    return render(request, 'answer_question.html',d)
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('QuestionList'))




