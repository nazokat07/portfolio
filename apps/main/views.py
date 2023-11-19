from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm



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
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})
    
    #print(ProductForm(request.POST).is_valid())
    #context = {
        #'form': form
    #}
    





