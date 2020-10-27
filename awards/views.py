from django.shortcuts import render,redirect
from .models import Project,Review,Profile
from .forms import ProjectUploadForm,ProfileUpdateForm, ReviewForm,ImageProfileForm
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm
from .serializer import ProjectSerializer, ProfileSerializer
from django.contrib.auth.decorators import login_required



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

def myProfile(request,**kwargs):
    current_user=request.user
    prof_update=ProfileUpdateForm(request.POST)
    user_posts=Project.objects.filter(user=current_user.id)
    if prof_update.is_valid():
        profile=prof_update.save(commit=False)
        profile.user=current_user
        profile.save()
        return HttpResponseRedirect(request.path_info)
    else:
        prof_update=ProfileUpdateForm()
    context={
        'current_user':current_user,
        'prof_update':prof_update,
        'user_posts':user_posts,
    }
    return render(request, 'profile.html', locals())

def details(request, id):
    current_site=Project.single_project(id)
    current_user=request.user
    proj_reviews=Review.objects.filter(project=current_site)
    review_form=ReviewForm(request.POST)
    if review_form.is_valid():
        review=review_form.save(commit=False)
        review.user=current_user
        review.project=current_site
        review.save()
        return HttpResponseRedirect(request.path_info)
    else:
        review_form=ReviewForm()
    context={
        'current_user':current_user,
        'current_site':current_site,
        'review_form':review_form,
        'proj_reviews':proj_reviews,
    }
    return render(request, 'details.html',locals())


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_project})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ImageProfileForm()
        return render(request,'edit_profile.html',{"form":form})

class Profile_list(APIView):
    def get(self, request, format=None):
        all_profile=Profile.objects.all()
        serializers=ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class Project_list(APIView):
    def get(self,request,format=None):
        all_projects=Project.objects.all()
        serializers=ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)


@login_required(login_url='/accounts/login/')
def project_review(request,project_id):
    try:
        single_project = Project.get_single_project(project_id)
        average_score = round(((single_project.design + single_project.usability + single_project.content)/3),2)
        if request.method == 'POST':
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                single_project.vote_submissions+=1
                if single_project.design == 0:
                    single_project.design = int(request.POST['design'])
                else:
                    single_project.design = (single_project.design + int(request.POST['design']))/2
                if single_project.usability == 0:
                    single_project.usability = int(request.POST['usability'])
                else:
                    single_project.usability = (single_project.usability + int(request.POST['usability']))/2
                if single_project.content == 0:
                    single_project.content = int(request.POST['content'])
                else:
                    single_project.content = (single_project.content + int(request.POST['usability']))/2

                single_project.save()
                return redirect('project_review',project_id)
        else:
            vote_form = VoteForm()

    except Exception as  e:
        raise Http404()
    return render(request,'project_review.html',{"vote_form":vote_form,"single_project":single_project,"average_score":average_score})
