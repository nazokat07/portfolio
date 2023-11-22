from django.shortcuts import render, redirect

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def admin(request):
    return render(request, 'admin.html')

def allpost(request):
    return render(request, 'allpost.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    if request.method == 'POST':
            return redirect(to='home')
    return render(request, 'index.html')
    
    
    





