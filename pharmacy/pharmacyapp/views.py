from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm
from .models import Category, Product

# Create your views here.
def home(request):
    return render(request, 'index.html')

def categories(request):
    all_categories = Category.objects.all().values()
    categories_dict = {"category" : all_categories}
    return render(request, 'categories.html', categories_dict)


def about(request):
    return render(request, 'about.html')


def contact(request):

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'contact.html', {"form": form})


def products(request, id):

    items = Product.objects.filter(categoryID = id)
    productDict = {"products": items}

    return render(request, 'products.html', productDict)