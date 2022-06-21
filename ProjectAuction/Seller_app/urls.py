from django.urls import path
from . import views

urlpatterns = [
    path('ctf/', views.AddProductCategory.as_view(), name = 'addcategory_url'),
    path('scl/', views.ProductCategoryList.as_view(), name = 'showcategory_url'),
    path('uct/<int:pk>/', views.UpdateProductCategory.as_view(), name = 'updatecategory_url'),
    path('dct/<int:pk>/', views.DeleteProductCategory.as_view(), name = 'deletecategory_url'),

    path('subf/', views.AddProductSubCategory.as_view(), name = 'addsubcategory_url'),
    path('subl/', views.ProductSubCategoryList.as_view(), name = 'showsubcategory_url'),
    path('usub/<int:pk>/', views.UpdateProductSubCategory.as_view(), name = 'updatesubcategory_url'),
    path('dsub/<int:pk>/', views.DeleteProductSubCategory.as_view(), name = 'deletesubcategory_url'),

    path('pif/', views.AddProductInformation.as_view(), name = 'addproinfo_url'),
    path('pil/', views.ProductInformationList.as_view(), name = 'showproinfo_url'),
    path('upi/<int:pk>/', views.UpdateProductInformation.as_view(), name = 'updateproinfo_url'),
    path('dpi/<int:pk>/', views.DeleteProductInformation.as_view(), name = 'deleteproinfo_url'),

    path('pimf/', views.AddProductImages.as_view(), name = 'addproimg_url'),
    path('piml/', views.ProductImagesList.as_view(), name = 'showproimg_url'),
    path('upim/<int:pk>/', views.UpdateProductImages.as_view(), name = 'updateproimg_url'),
    path('dpim/<int:pk>/', views.DeleteProductImages.as_view(), name = 'deleteproimg_url')

]