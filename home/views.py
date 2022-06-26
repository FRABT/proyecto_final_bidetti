from django.shortcuts import render
from django.db.models import Q

#from user.models import Avatar


def index(request):
    return render(request, "home/main.html")

def about(request):
    return render(request, "home/about.html")

#def get_avatar_url_ctx(request):
#    avatars = Avatar.objects.filter(user=request.user.id)
#    if avatars.exists():
#        return {"url": avatars[0].image.url}
#    return {}