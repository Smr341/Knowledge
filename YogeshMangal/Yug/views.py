from django.http import HttpResponse
from django.shortcuts import render
from Yug.models import Contact
#admin and #Yogesh@1234
# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        pass1=request.POST.get('pass1')
        knlg=request.POST.get('knlg')
        contact=Contact(name=name,pass1=pass1,knlg=knlg)
        contact.save()

    return render(request,'index.html')