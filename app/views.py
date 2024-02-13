from django.shortcuts import render
from app.forms import *
from django.http import *

# Create your views here.
def insert_topicforms(request):
    ETFO=Topicforms()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicforms(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topicforms is done ')


    return render(request,'insert_topicforms.html',d)

def insert_webpageforms(request):
    EWFO=Webpageforms()
    d={'EWFO':EWFO}
    if request.method=='POST':
        EWDO=Webpageforms(request.POST)
        if EWDO.is_valid():
            EWDO.save()
            return HttpResponse('insert_webpageforms is done ')
    return render(request,'insert_webpageforms.html',d)

def insert_accessrecordforms(request):
    EAFO=Accessrecordforms()
    d={'EAFO':EAFO}
    if request.method=='POST':
        EADO=Accessrecordforms(request.POST)
        if EADO.is_valid():
            EADO.save()
            return HttpResponse('insert_accessrecordforms is done')
    return render(request,'insert_accessrecordforms.html',d)