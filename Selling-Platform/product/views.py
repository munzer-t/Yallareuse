from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from .forms import ProductFileForm
from .models import Attachment, Category, Product

User = get_user_model()


def create_product_view(request):
    user = request.user
    if user.is_authenticated:
        if user.user_type == User.UserTypePrivate.SELLER:
            if request.method == 'POST':
                form = ProductFileForm(request.POST, request.FILES)
                files = request.FILES.getlist('file')
                print('before valid')
                if form.is_valid():
                    print('after valid')
                    product = form.save(commit=True)
                    if files:
                        for file in files:
                            Attachment.objects.create(product=product, file=file)
                    
                    return redirect('product_list_initial')
            else:
                form = ProductFileForm()
            return render(request, 'product_creation.html', {'form':form})
        else:
            return redirect('product_list_initial')
    
    return redirect('login')


def product_list_view(request, category=None):
    user = request.user
    if user.is_authenticated:
        if request.method == 'GET':
            categories = Category.objects.all()
            if category is None:
                category = categories.first()

            products = Product.objects.prefetch_related('images').filter(category=category)
            context = {
                'categories': categories,
                'products': products
            }
            return render(request, 'product_main_page.html', context)
    return redirect('login')

def product_detail_view(request, product=None):
    user = request.user
    if user.is_authenticated:
        if request.method == 'GET':
            product = Product.objects.filter(id=product).first()
            context = {
                'product': product
            }
            return render(request, 'product_full_detail.html', context)
    return redirect('login')