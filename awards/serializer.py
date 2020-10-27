
from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('user.username','avi','bio')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('user','title','landing','description','live_site')