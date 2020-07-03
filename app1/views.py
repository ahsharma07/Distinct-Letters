from django.shortcuts import render
from django.http import HttpResponse
def homeview(request):
    d1={}
    if request.method=="POST":
        text=request.POST.get('text')
        text1=""
        for element in text:
            if element not in text1:
                text1=text1+element
        d1['answer']=text1
    return render(request,'app1/homepage.html',context=d1)
# Create your views here.
