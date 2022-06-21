from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import * 
from .forms import *

# Create your views here.
#PAYMENT APP
class PaymentList(ListView):
    model = Payment

class AddPayment(CreateView):
    model = Payment
    fields = '__all__'
    success_url = reverse_lazy('showpayment_url')

class UpdatePayment(UpdateView):
    model = Payment
    fields = '__all__'
    success_url = reverse_lazy('showpayment_url')

class DeletePayemnt(DeleteView):
    model = Payment
    fields = '__all__'
    success_url = reverse_lazy('showpayment_url')
