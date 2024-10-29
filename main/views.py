
from django.shortcuts import render, redirect
from .models import Product,Log
from .forms import Productform

def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = Productform(request.POST)
        if form.is_valid():
            product = form.save()
            Log.objects.create(
                log_type='CREATE',
                product=product,
                message=f'New product created: {product.title} (ID: {(Product.id)})'
            )
            return redirect('product_list')
    else:
        form = Productform()
    return render(request, 'main/create_product.html', {'form': form})

def update_product(request,id):
    product = Product.objects.get(id=id)
    old_name = product.title
    if request.method == 'POST':
        form = Productform(request.POST, instance=product)
        if form.is_valid():
            form.save()
            Log.objects.create(
                log_type='UPDATE',
                product=product,
                message=f'Updated product {id}: old name={old_name}, new name={product.title}'
            )
            return redirect('product_list')
    else:
        form = Productform(instance=product)
    return render(request, 'main/update_product.html', {'form': form})
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_list')