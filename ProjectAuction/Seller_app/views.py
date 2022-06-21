from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
#PRODCUT_CATEGORY
class ProductCategoryList(ListView):
    model = ProductCategory

class AddProductCategory(CreateView):
    model = ProductCategory
    fields = '__all__'
    success_url = reverse_lazy('showcategory_url')

class UpdateProductCategory(UpdateView):
    model = ProductCategory
    fields = '__all__'
    success_url = reverse_lazy('showcategory_url')

class DeleteProductCategory(DeleteView):
    model = ProductCategory
    fields = '__all__'
    success_url = reverse_lazy('showcategory_url')
    context_object_name = 'object_list'

#PRODUCT_SUB_CATEGORY
class ProductSubCategoryList(ListView):
    model = ProductSubCategory

class AddProductSubCategory(CreateView):
    model = ProductSubCategory
    fields = '__all__'
    template_name = 'Seller_app/productsubcategory_form.html'
    success_url = reverse_lazy('showsubcategory_url')

class UpdateProductSubCategory(UpdateView):
    model = ProductSubCategory
    fields = '__all__'
    success_url = reverse_lazy('showsubcategory_url')

class DeleteProductSubCategory(DeleteView):
    model = ProductSubCategory
    fields = '__all__'
    success_url = reverse_lazy('showsubcategory_url')
    context_object_name = 'object_list'

#PRODUCT INFORMATION
class ProductInformationList(ListView):
    model = ProductInformation

class AddProductInformation(CreateView):
    model = ProductInformation
    fields = '__all__'
    success_url = reverse_lazy('showprodinfo_url')

class UpdateProductInformation(UpdateView):
    model = ProductInformation
    fields = '__all__'
    success_url = reverse_lazy('showprodinfo_url')

class DeleteProductInformation(DeleteView):
    model = ProductInformation
    fields = '__all__'
    success_url = reverse_lazy('showprodinfo_url')
    context_object_name = 'object_list'

#PRODUCT IMAGES
class ProductImagesList(ListView):
    model = ProductImages
    paginate_by = 2

class AddProductImages(CreateView):
    model = ProductImages
    fields = '__all__'
    success_url = reverse_lazy('showproimg_url')

class UpdateProductImages(UpdateView):
    model = ProductImages
    fields = '__all__'
    success_url = reverse_lazy('showproimg_url')

class DeleteProductImages(DeleteView):
    model = ProductImages
    fields = '__all__'
    success_url = reverse_lazy('showproimg_url')
    context_object_name = 'object_list'