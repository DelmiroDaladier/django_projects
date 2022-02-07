from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shortener/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        print(f'uid:{uid}')
        return HttpResponse(uid)

def follow_link(request, pk):
    url_object = Url.objects.get(uuid=pk)
    return redirect('https://'+ url_object.link)