from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm



def index(request):
    return render(request,'index.html')


def projects(request):
    return render(request,'projects.html')


def registration(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
    else:
        form = ProductForm()
    return render(request, 'registration.html', {'form': form})
    
    #print(ProductForm(request.POST).is_valid())
    #context = {
        #'form': form
    #}
    





