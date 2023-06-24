from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import MyCreationForm
from .models import ChatText
from .serielizer import ChatSerializer

# Create your views here.
@login_required(login_url="/login")
def home(request):
    users=[i.username for i in User.objects.all() if not i.is_superuser]
    users.remove(request.user.username)
    return render(request,'index.html',{"users":users})

def get_chat(request):
    receiver=request.GET.get('receiver')
    receiver=User.objects.get(username=receiver)
    chat_messages = ChatText.objects.filter(sender=request.user, receiver=receiver) | ChatText.objects.filter(sender=receiver, receiver=request.user).order_by('time')
    chat_messages=ChatSerializer(chat_messages,many=True)
    return JsonResponse(data=chat_messages.data,safe=False)

def signup(request):
    context={
        'action':'signup',
        'btn_type':'Sign Up',
        'change_url':'login',
        'change_text':"Already have account"
    }
    if request.method=="POST":
        userForm=MyCreationForm(request.POST)
        print(userForm.is_valid())
        print(userForm.cleaned_data)
        if userForm.is_valid():
            userForm.save()
            return redirect('/login')
        else:
            context['error']="User already exist"
        
    return render(request,'login.html',context=context)
def _login(request):
    context={
        'action':'login',
        'btn_type':'Login',
        'change_url':'signup',
        'change_text':"Don't have account"
    }
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        print(username,password)
        user=auth.authenticate(request=request,username=username,password=password)
        print(user)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            context['error']="Invalid credentials"
    
    return render(request,'login.html',context=context)


def _logout(request):
    auth.logout(request)
    return redirect('/')