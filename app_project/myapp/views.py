from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm 

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Contact form submitted successfully.")
    return HttpResponse("Invalid request method.")