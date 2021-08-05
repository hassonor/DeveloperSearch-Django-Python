from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profile.html', context)

def userProfile(request, pk):
    return render(request, 'users/user-profile.html')