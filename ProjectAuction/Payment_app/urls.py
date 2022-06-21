from django.urls import path
from . import views

urlpatterns = [
    path('pf/', views.AddPayment.as_view(), name='paymentform_url'),
    path('sp/', views.PaymentList.as_view(), name='showpayment_url'),
    path('up/<int:pk>/', views.UpdatePayment.as_view(), name='updatepayemnt_url'),
    path('dp/<int:pk>/', views.DeletePayemnt.as_view(), name='deletepayment_url')
]