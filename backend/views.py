from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
    return HttpResponse("This is home page")

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        product = models.Product(name=name, price=price, quantity=quantity, description=description)
        product.save()
        return redirect('product_list')
    return render(request, 'inventory/create_product.html')

def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})
def update_product(request,id):
    products=get_object_or_404(models.Product,id=id)
    if request.method=='POST':
        products.name=request.POST.get('name')
        products.price=request.POST.get('price')
        products.quantity=request.POST.get('quantity')
        products.description=request.POST.get('description')
        products.save()
        return redirect('product_list')
    return render(request,'inventory/update_product.html',{'products':products})

def delete_product(request,id):
    products=get_object_or_404(models.Product,id=id)
    products.delete()
    return redirect('product_list')
from .forms import ApplicationForm 

def index(request): 
    form = ApplicationForm() 

    return render(request, 'inventory/application_form.html', {'form': form}) 
