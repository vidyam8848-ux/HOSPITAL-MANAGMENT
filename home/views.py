from django.shortcuts import render
from django.http import HttpResponse
from . models import dept,Doctors,booking
from django.shortcuts import render, redirect
from .forms import BookingForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  
    return render(request,'index.html')

@login_required
def about(request):
    
    return render(request,'about.html')


@login_required
def doctors(request):
    data = Doctors.objects.all()
    dict_doc = {
        'doctors' : data
    }
    return render(request,'doctors.html',dict_doc)

@login_required
def department(request):
    dic_dept = {
        'dept1' : dept.objects.all()
   }
  
    return render(request,'department.html',dic_dept)
  
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')    
        
    else:
        form = UserCreationForm()
    return render(request,'signup.html', {'form': form})    

@login_required
def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = BookingForm()
    
    return render(request,'booking.html', {'form': form})