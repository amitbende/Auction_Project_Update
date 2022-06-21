from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
#SUCCESS REPORT
class SuccessReportList(ListView):
    model = SuccessReport

class AddSuccessReport(CreateView):
    model = SuccessReport
    fields = '__all__'
    success_url = reverse_lazy('showsuccess_url')

class UpdateSuccessReport(UpdateView):
    model = SuccessReport
    fields = '__all__'
    success_url = reverse_lazy('showsuccess_url')

class DeleteSuccessReport(DeleteView):
    model = SuccessReport
    fields = '__all__'
    success_url = reverse_lazy('showsuccess_url')
    context_object_name = 'object_list'

#CANCEL REPORT
class CancelReportList(ListView):
    model = CancelReport

class AddCancelReport(CreateView):
    model = CancelReport
    fields = '__all__'
    success_url = reverse_lazy('showcancel_url')

class UpdateCancelReport(UpdateView):
    model = CancelReport
    fields = '__all__'
    success_url = reverse_lazy('showcancel_url')

class DeleteCancelReport(DeleteView):
    model = CancelReport
    fields = '__all__'
    success_url = reverse_lazy('showcancel_url')
    context_object_name = 'object_list'

#AUCTION QUERY
class AuctionQueryList(ListView):
    model = AuctionQuery

class AddAuctionQuery(CreateView):
    model = AuctionQuery
    fields = '__all__'
    success_url = reverse_lazy('showquery_url')

class UpdateAuctionQuery(UpdateView):
    model = AuctionQuery
    fields = '__all__'
    success_url = reverse_lazy('showquery_url')

class DeleteAuctionQuery(DeleteView):
    model = AuctionQuery
    fields = '__all__'
    success_url = reverse_lazy('showquery_url')
    context_object_name = 'object_list'

#FEEDBACK
class FeedBackList(ListView):
    model = FeedBack

class AddFeedBack(CreateView):
    model = FeedBack
    fields = '__all__'
    success_url = reverse_lazy('showfeedback_url')

class UpdateFeedBack(UpdateView):
    model = FeedBack
    fields = '__all__'
    success_url = reverse_lazy('showfeedback_url')

class DeleteFeedBack(DeleteView):
    model = FeedBack
    fields = '__all__'
    success_url = reverse_lazy('showfeedback_url')
    context_object_name = 'object_list'
