from email import message
from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse, JsonResponse
from .view_helpers import create as create_helper

# Create your views here.
def index(request):
    return render(request, 'shortener/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']

        if create_helper.check_url(link):
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=link, uuid=uid)
            new_url.save()
            print(f'uid:{uid}')
            return HttpResponse(uid)
        else:
            message = 'URL is not valid!'

            response = JsonResponse({"error": message}, status=400)
            return response

def follow_link(request, pk):
    url_object = Url.objects.get(uuid=pk)
    return redirect('https://'+ url_object.link)