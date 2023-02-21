from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def app2(request):
    return render(request,'app_2/app2.html')
def apps(request,page_id):
    return render(request, 'app_2/apps.html', context={'page_id':page_id})