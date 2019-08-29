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
from django.db.models import Count



# Create your views here.
def index(request):
    """return index page"""
    #get count for statics tables on home page
    inqueue_count = Bug.objects.filter(status='q').count()
    inprogrss_count = Bug.objects.filter(status='p').count()
    complete_count = Bug.objects.filter(status='c').count()
    total_bug_count = Bug.objects.all().count()
    
    finqueue_count = Feature.objects.filter(status='q').count()
    finprogrss_count = Feature.objects.filter(status='p').count()
    fcomplete_count = Feature.objects.filter(status='c').count()
    total_feature_count = Feature.objects.all().count()
    
    return render(request,'index.html',{"queue_count":inqueue_count , "progress_count":inprogrss_count, "complete_count":complete_count ,"bug_total":total_bug_count , "fqueue_count":finqueue_count , "fprogress_count":finprogrss_count, "fcomplete_count":fcomplete_count ,"feature_total":total_feature_count})
  
@login_required 
def logout(request):
    """log user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """return a login page"""
    # if member is already logged in return to profile page
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    #if form submitted then take details
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        #if valid form then check details
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        #if correct, login user and  redirect to home pag
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('profile'))
        #else display error message
            else:
                messages.error(request, "Your username or password is incorrect")
    else:
        #if not post them display form
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    
    
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
     # if post collect form details   
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        # if form valid the write to database
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
        #if user okay then go to index page and display message else display error messgae                            
            if user:
                auth.login(user=user, request=request)
                messages.success(request,"You have sucessfully registered")
                return redirect(reverse('profile'))
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
    #get bugs that user created with the ones with the top votes at the top
    bugs = Bug.objects.filter(author=name).order_by('-vote')
    #get features that user created with the ones with the top votes at the top
    features = Feature.objects.filter(author=name).order_by('-vote')
    return render(request, "profile.html", {"profile": user , "bugs":bugs , "features":features})
        
def statistics(request):
	return render(request, 'dashboard.html')   
''' remaining functions are to get data for graph '''

#gets tops 5 bugs by most votes
def getdata_bug(self):
    bugs = list(Bug.objects.values('name','vote').order_by('-vote')[:5])
    return JsonResponse(bugs, safe=False)

#gets tops 5 features by most votes    
def getdata_feature(self):
    features = list(Feature.objects.values('name','vote').order_by('-vote')[:5])
    return JsonResponse(features, safe=False)
    
# gets top 5 author and count of bugs they created
def getdata_bug_user(self):
    bugs = list(Bug.objects.values('author__username').annotate(count=Count('author')).order_by('-count')[:5])
    return JsonResponse(bugs, safe=False)

# gets top 5 authorand count if features they created
def getdata_feature_user(self):
    features = list(Feature.objects.values('author__username').annotate(count=Count('author')).order_by('-count')[:5])
    return JsonResponse(features, safe=False)
    

# gets count of all bugs and features 
def bug_feature_count(self):
    total_bug_count = Bug.objects.all().count()
    total_feature_count = Feature.objects.all().count()
    g = json.dumps([{ "name":'bugs', "count": total_bug_count}, {"name":'Features', "count": total_feature_count} ])
    return HttpResponse(g, content_type='application/json')
    