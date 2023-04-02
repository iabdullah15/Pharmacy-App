from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('categories', views.categories, name="categories"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    path('products/<int:id>', views.products, name = "products"),
]