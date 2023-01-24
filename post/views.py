from django.shortcuts import render, HttpResponse
from post.models import Product, Comment, Category


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
        return render(request, 'posts/post.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product_obj = Product.objects.get(id=id)
        comments = Comment.objects.filter(post=product_obj)
        context = {
            'product': product_obj,
            'comments': comments
        }
        return render(request, 'posts/detail.html', context=context,)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)
