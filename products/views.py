from django.shortcuts import render,redirect
from products.models import Product, Comment, Category
from products.forms import ProductCreateForm, CommentCreateForm


# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'layosts/index.html')


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/product.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product_obj = Product.objects.get(id=id)
        comments = Comment.objects.filter(post=product_obj)
        form = CommentCreateForm (data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                title=form.cleaned_data.get('title'),
                product=product_obj
            )
            return redirect(f'/products/{product_obj.id}/')
        return render(request, 'products/detail.html', context={
            'product':product_obj,
            'comment':comments,
            'form':form
        })


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)

def create_product_view(request):
    if request.method =='GET':
        context = {
            'form':ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                title = form.cleaned_data.get('title'),
                description = form.cleaned_data.get('description'),
                price =form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 0,
                rate =form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5,
            )
            return redirect('/products')
        return render(request, 'products/create.html', context={
            'form': form
        })