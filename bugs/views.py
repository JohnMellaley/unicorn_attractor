from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Bug, UserBug
from .forms import BugForm
from django.contrib.auth.models import User
# Create your views here.

def all_bugs(request):
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})
    
def create_an_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vote = 0
            instance.author = request.user
            instance.status = 'q'
            instance.save()
            return redirect(all_bugs)
    else:
        form = BugForm()

    return render(request, "bug_form.html", {'form': form})
    
def viewbug(request, bugid):
    mybug = Bug.objects.get(id=bugid)
    return render (request, "viewbug.html", {"bug": mybug})
    
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
            print("not inquery")
            return JsonResponse({"error":"You are the author of this recipe"});
    else:
    # user voted for this bug before
        return JsonResponse({"error":"You voted for this before"});
       
        
    return JsonResponse({"success":"data updated", "likes": mybug.vote})
    