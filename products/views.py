from django.shortcuts import render, redirect
from products.models import Product, Comment, Category
from products.forms import ProductCreateForm, CommentCreateForm


# Create your views here.
PAGINATION_LIMIT = 3


def main(request):
    if request.method == 'GET':
        return render(request, 'layosts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        category_id = request.GET.get('category')
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        if search is not None:
            products = Product.objects.filter(
                title__icontains=search
            )

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        if category_id:
            products = Product.objects.filter(category=Category.objects.get(id=category_id))

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page+1)
        }
        return render(request, 'products/products.html', context=context)

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layosts/index.html')


def product_detail_view(request, id):
    if request.method == 'GET':
        product_obj = Product.objects.get(id=id)
        reviews = Comment.objects.filter(product=product_obj)

        context = {
            'product': product_obj,
            'reviews': reviews,
            'form': CommentCreateForm
        }
        return render(request, 'products/detail.html', context=context)
    if request.method == 'POST':
        product_obj = Product.objects.get(id=id)
        reviews = Comment.objects.filter(product=product_obj)
        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                title=form.cleaned_data.get('title'),
                product=product_obj
            )
            return redirect(f'/products/{product_obj.id}/')
        return render(request, 'products/detail.html', context={
            'product': product_obj,
            'reviews': reviews,
            'form': form
        })



def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }

        return render(request, 'categories/index.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 0,
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5,
            )
            return redirect('/products/')
        return render(request, 'products/create.html', context={
            'form': form
        })