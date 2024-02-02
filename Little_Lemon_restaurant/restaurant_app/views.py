from django.shortcuts import render, redirect
from .models import Menu,Booking
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import BookingForm
from datetime import timedelta,datetime

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'about.html')
def menu(request):
    menu_data=Menu.objects.all()
    main_data={'menu': menu_data}
    return render(request, 'menu.html', main_data)
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('book')
        else:
            messages.success(request,("Your username or password is wrong.\n Try again!!!"))
            return redirect('login')
    else:
        return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('login')
def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Registration success"))
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})
def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            target_date = form.cleaned_data['date']
            target_time = form.cleaned_data['time']
            target_datetime = datetime.combine(target_date, target_time)
            end_time = target_datetime + timedelta(hours=3)
            
            existing_bookings = Booking.objects.filter(date=target_date, time__range=(target_time, end_time.time()))
            
            if existing_bookings.count() <= 2:
                Booking.objects.create(name=name, date=target_date, time=target_time, bookings_count=existing_bookings.count() + 1)
                return redirect('home')
            else:
                messages.error(request, "Booking limit reached for this date and time.")
        else:
            messages.error(request, "Invalid form submission. Please check your input.")
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})

    

        
    