from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import JsonResponse
from .models import Bug, UserBug, Post
from .forms import BugForm, BlogPostForm
from django.contrib.auth.models import User

# Create your views here.
#shows all bugs with bug with most votes firsr
def all_bugs(request):
    bugs = Bug.objects.all().order_by('-vote')
    return render(request, "bugs.html", {"bugs": bugs})
    
#create a bug
def create_an_bug(request):
    #get info from form
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES)
        #if forn valid safe to file and these fields up that are not on the form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vote = 0
            instance.author = request.user
            instance.status = 'q'
            instance.save()
            return redirect(all_bugs)
    else:
        #else display form
        form = BugForm()

    return render(request, "bug_form.html", {'form': form})
 
#view bug with id provided and posts associated with that   
def viewbug(request, bugid):
    mybug = Bug.objects.get(id=bugid)
    posts = Post.objects.filter(bugid=mybug.id)
    return render (request, "viewbug.html", {"bug": mybug, "posts":posts})
    
   
def create_post_bug(request, bugid):
    """
    Create a view that allows us to create
     a post
    """
    #get details from form
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        bug = Bug.objects.get(id=bugid)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.bugid = bug
            instance.save()
            return redirect("viewbug", bugid)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})
    
def likes(request):
    # get bug id
    mybugid = request.GET.get('bug_id')
    # get bug with that id
    mybug = Bug.objects.get(id=mybugid)
    #check in Userbug table how may time the bug is there 
    bugquery = UserBug.objects.filter(bugid=mybugid)
    # check if user is in the bugquery list
    userquery = bugquery.filter(userid=request.user)
    #if not that user can like this bug
    if not userquery:
        if mybug.author != request.user:
            mybug.vote += 1
            mybug.save()
            buglike = UserBug(userid = request.user , bugid = mybug)
            buglike.save()
        else:
            return JsonResponse({"error":"You are the author of this bug"});
    else:
    # user voted for this bug before
        return JsonResponse({"error":"You voted for this before"});
       
        
    return JsonResponse({"success":"data updated", "likes": mybug.vote})
    