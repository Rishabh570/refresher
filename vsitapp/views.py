import requests
from forms import HelpForm
from vsitapp.models import Post
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# TODO: Remove this function and merge this in home_login
def home(request):
    if request.method == 'POST':
        userName = request.POST['username']
        passWord = request.POST['password']
        user = authenticate(request, username=userName, password=passWord)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse('User doesn\'t exist')
    else:
        return render(request, 'home.html')

# Main Home landing page
def home_login(request):
    return render(request, 'home_loggedin.html')

def list(request):

    # --------------------------------POST method on lists---------------------------------------------
    if request.method == 'POST':

        ''' Begin reCAPTCHA validation '''
        re_response = request.POST["g-recaptcha-response"]
        data = {
            "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            "response": re_response,
        }
        res = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)

        if res.json()['success']:
            title_lower = request.POST.get('title').lower()
            author = request.user.first_name + request.user.last_name
            profile = Post.objects.create(name=request.user.first_name, title=title_lower, story=request.POST.get('story'), author=author)
            return HttpResponseRedirect('/list/')
        else:
            return HttpResponseRedirect(r'/help/')

    # -------------------------------GET method on lists--------------------------------------------------
    elif request.method == 'GET':
        if request.GET.get('title'):
            title_search = request.GET.get('title').lower()
            profile = Post.objects.filter(title=title_search)
        else:
            profile = Post.objects.all()
        return render(request, 'list.html', {'profile': profile})

@login_required()
def help(request):
    try:
        profile_url = 'https://api.github.com/search/users?q={}'.format(request.user.username)
        response = requests.get(profile_url).json()
        avatar = response['items'][0]['avatar_url']
    except:
        avatar = None
    return render(request, 'help_form.html', {'profile': avatar})

# TODO: Remove this function, this is just for flushing all database entries
def drop(request):
    profile_nill = Post.objects.all().delete()
    return HttpResponseRedirect('/list')

# Function for logging user in
def loginuser(request):
    return render(request, 'login.html')

# Function for logging user out
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/home_login/')

# Utility function
def get_user(request):
    current_user = request.user
    return HttpResponse('current_user name is: ' + str(current_user.first_name) + ' ' + str(current_user.last_name))

# Function for upVote feature
def upvote(request):
    filter = request.GET.get('filter')
    query = Post.objects.get(id=filter)
    query.votes.up(request.user.id)
    votes = query.votes.count()
    query.votings = votes
    query.save()
    return HttpResponse(votes)

# Function for downVote feature
def downvote(request):
    filter = request.GET.get('filter')
    query = Post.objects.get(id=filter)
    query.votes.down(request.user.id)
    votes = query.votes.count()
    query.votings = votes
    query.save()
    return HttpResponse(votes)

# Function for Deleting a Post, that's why requires LoggedIn User
@login_required
def delete_post(request):
    post_id = request.GET.get('post_id')
    query = Post.objects.get(id=post_id)
    post_author = query.author
    user_name = request.user.first_name + request.user.last_name
    if (user_name == post_author):
        query.delete()
        return HttpResponse('Success')
    else:
        return HttpResponse('You are not authorized to delete this record')
