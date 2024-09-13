from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

# Create your views here.
def student_list(request):
    std = Students.objects.all()
    return render(request,'student_list.html',{'students':std})

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def  profile(request):
    return render(request,'profile.html')