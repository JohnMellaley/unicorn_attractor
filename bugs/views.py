from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Bug
from .forms import BugForm
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
    
def likes(self):
    print ("test")
    return JsonResponse({"success":"data updated"})