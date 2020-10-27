from django.shortcuts import render,redirect
from .models import Project,Review,Profile
from .forms import ProjectUploadForm,ProfileUpdateForm, ReviewForm,ImageProfileForm
from django.http import HttpResponseRedirect
from rest_framework.response import Response

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("login")
    return render(request,"accounts/register.html",{"form":form})

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request,**kwargs):
    projects=Project.objects.all()[::-1]
    proj_upload=ProjectUploadForm(request.POST, request.FILES)
    if proj_upload.is_valid():
        projo=proj_upload.save(commit=False)
        projo.user=request.user
        projo.save()
        return HttpResponseRedirect(request.path_info)
    else:
        proj_upload=ProjectUploadForm()
    context={
        'projects':projects,
        'proj_upload':proj_upload,
    }

    return render(request, 'index.html', locals())