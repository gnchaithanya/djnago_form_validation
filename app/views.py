from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sage=SFDO.cleaned_data['Sage']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']

            so=Student.objects.get_or_create(Sname=Sname,Sage=Sage,Sid=Sid,Semail=Semail)[0]
            so.save()
            QSO=Student.objects.all()
            d1={'QSO':QSO}
            return HttpResponse(str(SFDO.cleaned_data))
            # return render(request,'display_student.html',d1)
            # return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid Data!!!')

    
    return render(request,'student.html',d)

def update_student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=request.POST['Sname']
            Sage=request.POST['Sage']
            Sid=request.POST['Sid']
            Semail=request.POST['Semail']
            Student.objects.filter(Sname=Sname).update(Sage=Sage,Sid=Sid,Semail=Semail)
            QSO=Student.objects.all()
            d1={'QSO':QSO}
            return render(request,'display_student.html',d1)
        else:
            return HttpResponse('Invalid Data!!!')
        
    return render(request,'update_student.html',d)
def delete_student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method=='POST':
       SFDO=StudentForm(request.POST)
       if SFDO.is_valid():
            Sname=request.POST['Sname']
            Student.objects.filter(Sname=Sname).delete()
            QSO=Student.objects.all()
            d1={'QSO':QSO}
            
            return render(request,'display_student.html',d1)
       else:
            return HttpResponse('Invalid Data!!!')
            
    return render(request,'delete_student.html',d)
        