from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import Note
from .forms import EntryForm
from django.utils import timezone
from django.contrib import messages
def hii(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in ['surendra','jobin'] and password in ['surendra#','Jobinkv#']:        
            messages.success(request, 'You have been logged in successfully.')
            return redirect('dashboard')
        else:          
            return render(request,'invalid.html')
    return render(request,'hello.html')

def dashboard_view(request):
    form=EntryForm()
    entries=Note.objects.all()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request,'dashboard.html',{'form':form,'entries':entries,'current_time': timezone.now()})
# Create your views here.
def delete_entry(request, id):
    entry = get_object_or_404(Note, id=id)
    entry.delete()
    return redirect('dashboard')
def update_entry(request, id):
    entry = get_object_or_404(Note, id=id)
    form = EntryForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'update_entry.html', {'form': form, 'entry': entry})

