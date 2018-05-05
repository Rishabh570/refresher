import requests
from forms import HelpForm
from .forms import RegisterForm
from django.urls import reverse
from vsitapp.models import Post
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


'''
================================
Home Page View
================================
'''
def home_login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        passWord = request.POST['password']
        user = authenticate(request, username=userName, password=passWord)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home_login/')
        else:
            return HttpResponse('User doesn\'t exist')
    return render(request, 'home_loggedin.html')


'''
================================
Stories View
================================
'''
def list(request):
    # POST METHOD =======================================
    if request.method == 'POST':

        ''' Begin reCAPTCHA validation '''
        re_response = request.POST["g-recaptcha-response"]
        data = {
            "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            "response": re_response,
        }
        res = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data).json()

        if res['success']:
            title_lower = request.POST.get('title').lower()
            author = request.user.username
            profile = Post.objects.create(first_name=request.user.first_name, title=title_lower, story=request.POST.get('story'), author=author)
            return HttpResponseRedirect('/list/')
        else:
            return HttpResponseRedirect('/help/')

    # GET METHOD =========================================
    elif request.method == 'GET':
        if request.GET.get('title'):
            title_search = request.GET.get('title').lower()
            profile = Post.objects.filter(title=title_search)
        else:
            profile = Post.objects.all()
        return render(request, 'list.html', {'profile': profile})


'''
================================
Help-form submission View
================================
'''
@login_required(login_url='/login/')
def help(request):
    try:
        profile_url = 'https://api.github.com/search/users?q={}'.format(request.user.username)
        response = requests.get(profile_url).json()
        avatar = response['items'][0]['avatar_url']
    except:
        avatar = None
    return render(request, 'help_form.html', {'profile': avatar})


'''
=============================================================================
TODO: Remove this function, this is just for flushing all database entries
=============================================================================
'''
def drop(request):
    Post.objects.all().delete()
    return HttpResponseRedirect('/list')


'''
================================
Sign-Up View
================================
'''
def sign_up(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            print(form.errors)
    return render(request, 'sign_up.html', {'form': form})


'''
================================
Log-In View
================================
'''
def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home_login'))
    return render(request, 'login.html', {'form': form})


'''
================================
Log-Out View
================================
'''
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/home_login/')


'''
================================
Password Change View
================================
'''
def passchange(request):
    form  = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('home_login'))
    return render(request, 'passchangeform.html', {'form': form})


'''
================================
Up-Vote view
================================
'''
def upvote(request):
    filter = request.GET.get('filter')
    query = Post.objects.get(id=filter)
    query.votes.up(request.user.id)
    votes = query.votes.count()
    query.votings = votes
    query.save()
    return HttpResponse(votes)


'''
================================
 Down-Vote view
================================
'''
def downvote(request):
    filter = request.GET.get('filter')
    query = Post.objects.get(id=filter)
    query.votes.down(request.user.id)
    votes = query.votes.count()
    query.votings = votes
    query.save()
    return HttpResponse(votes)


'''
================================
Delete-Post view
================================
'''
def delete_post(request):
    post_id = request.GET.get('post_id')
    query = Post.objects.get(id=post_id)
    post_author = query.author
    user_name = request.user.username
    if (user_name == post_author):
        query.delete()
        return HttpResponse('Success')
    else:
        return HttpResponse('You are not authorized to delete this record')
