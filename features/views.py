from django.shortcuts import render, redirect
from .models import Feature
from .forms import FeatureForm
# Create your views here.

# Create your views here.
def all_features(request):
    features= Feature.objects.all()
    return render(request, "features.html",{"features":features})
    
def create_feature(request):
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.price = 100.00
            instance.author = request.user
            instance.save()
            return redirect(all_features)
    else:
        form = FeatureForm()
    return render(request, "feature_form.html", {'form': form})