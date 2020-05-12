from django.shortcuts import render
from .models import belowcontent

# Create your views here.
def home(request):
    obj=belowcontent.objects.all()
    return render(request,'home.html',{'obj':obj})

def claim_link(request):
    return render(request,'claiminfo.html')    

def claim_home(request):
    obj=belowcontent.objects.all()
    return render(request,'home.html',{'obj':obj})    

def renew_link(request):
    return render(request,'renewalinfo.html') 

def insure_link(request):
    return render(request,'insureinfo.html')    

    
