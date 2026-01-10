from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm, ParcelForm
from .models import Parcel, Tracking, CustomUser

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def add_parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            parcel = form.save(commit=False)
            parcel.user = request.user
            parcel.save()
            Tracking.objects.create(parcel=parcel, status='pending', notes='Parcel created')
            messages.success(request, 'Parcel added successfully.')
            return redirect('my_parcels')
    else:
        form = ParcelForm()
    return render(request, 'add_parcel.html', {'form': form})

@login_required
def my_parcels(request):
    parcels = Parcel.objects.filter(user=request.user)
    return render(request, 'my_parcels.html', {'parcels': parcels})

@login_required
def parcel_tracking(request, parcel_id):
    parcel = get_object_or_404(Parcel, id=parcel_id, user=request.user)
    trackings = parcel.trackings.all().order_by('-timestamp')
    return render(request, 'parcel_tracking.html', {'parcel': parcel, 'trackings': trackings})

@staff_member_required
def admin_dashboard(request):
    users = CustomUser.objects.all()
    parcels = Parcel.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users, 'parcels': parcels})

@staff_member_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, 'User deleted.')
    return redirect('admin_dashboard')

@staff_member_required
def update_parcel_status(request, parcel_id):
    parcel = get_object_or_404(Parcel, id=parcel_id)
    if request.method == 'POST':
        status = request.POST['status']
        location = request.POST.get('location', '')
        notes = request.POST.get('notes', '')
        parcel.status = status
        parcel.save()
        Tracking.objects.create(parcel=parcel, status=status, location=location, notes=notes)
        messages.success(request, 'Status updated.')
        return redirect('admin_dashboard')
    return render(request, 'update_status.html', {'parcel': parcel})
