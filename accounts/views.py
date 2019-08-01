import json
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.core.mail import send_mail
from bugs.models import Bug
from features.models import Feature
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View



# Create your views here.
def index(request):
    """return index page"""
    inqueue_count = Bug.objects.filter(status='q').count()
    inprogrss_count = Bug.objects.filter(status='p').count()
    complete_count = Bug.objects.filter(status='c').count()
    total_bug_count = Bug.objects.all().count()
    
    finqueue_count = Feature.objects.filter(status='q').count()
    finprogrss_count = Feature.objects.filter(status='p').count()
    fcomplete_count = Feature.objects.filter(status='c').count()
    total_feature_count = Feature.objects.all().count()
    
    return render(request,'index.html',{"queue_count":inqueue_count , "progress_count":inprogrss_count, "complete_count":complete_count ,"bug_total":total_bug_count , "fqueue_count":finqueue_count , "fprogress_count":finprogrss_count, "fcomplete_count":fcomplete_count ,"feauture_total":total_feature_count})
  
@login_required 
def logout(request):
    """log user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    
    
    
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request,"You have sucessfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:            
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', 
        {"registration_form" : registration_form})
        
def user_profile(request):
    """ this is the users profile page"""
    user = User.objects.get(email=request.user.email)
    name = request.user
    bugs = Bug.objects.filter(author=name)
    features = Feature.objects.filter(author=name)
    return render(request, "profile.html", {"profile": user , "bugs":bugs , "features":features})
        
def statistics(request):
	return render(request, 'dashboard.html')   
	
def getdata_bug(self):
    bugs = Bug.objects.all();
    c = json.dumps( [{'name': o.name, 'vote':o.id} for o in bugs] )
    return HttpResponse(c, content_type='application/json')
    
def getdata_feature(self):
    features = Feature.objects.all();
    d = json.dumps( [{'feature_name': o.name, 'feature_vote':o.id} for o in features] )
    return HttpResponse(d, content_type='application/json')
    
def getdata_bug_user(self):
    bugs = Bug.objects.all();
    e = json.dumps( [{'author': o.author.username, 'name': o.name} for o in bugs] )
    return HttpResponse(e, content_type='application/json')
    
def getdata_feature_user(self):
    features = Feature.objects.all();
    f = json.dumps( [{'author': o.author.username, 'name': o.name} for o in features] )
    return HttpResponse(f, content_type='application/json')
    
def bug_feature_count(self):
    total_bug_count = Bug.objects.all().count()
    total_feature_count = Feature.objects.all().count()
    g = json.dumps([{ "name":'bugs', "count": total_bug_count}, {"name":'Features', "count": total_feature_count} ])
    print(g)
    return HttpResponse(g, content_type='application/json')
    