from django import forms
from .models import Profile,Project,Review
SCORES = [
    (1,1),(2,2),
    (3,3),(4,4),
    (5,5),(6,6),
    (7,7),(8,8),
    (9,9),(10,10),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['user']

class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user','profile_Id']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=('comment', 'design', 'useability', 'content')
        widget={
            'comment':forms.Textarea(attrs={"class":"form-control mb-4"}),
            'design':forms.Select(choices=SCORES,attrs={"class":"form-control mb-4"}),
            'useability':forms.Select(choices=SCORES,attrs={"class":"form-control mb-4"}),
            'content':forms.Select(choices=SCORES,attrs={"class":"form-control mb-4"}),
        }    