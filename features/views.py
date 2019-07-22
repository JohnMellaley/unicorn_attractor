from django.shortcuts import render, redirect
from .models import Feature, PostFeature
from .forms import FeatureForm, BlogPostForm
# Create your views here.

# Create your views here.
def all_features(request):
    features= Feature.objects.all().order_by('-vote')
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
    
def viewfeature(request, featureid):
    myfeature = Feature.objects.get(id=featureid)
    posts = PostFeature.objects.filter(featureid=myfeature.id)
    return render (request, "viewfeature.html", {"feature": myfeature, "posts":posts})
    
 
def create_post(request, featureid):
    """
    Create a view that allows us to create
     a post
    """
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        feature = Feature.objects.get(id=featureid)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.featureid = feature
            instance.save()
            return redirect("viewfeature", featureid)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})