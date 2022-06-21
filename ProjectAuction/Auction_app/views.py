from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
#AUCTION DETAILS
class AuctionDetailsList(ListView):
    model = AuctionDetails

class AddAuctionDetails(CreateView):
    model = AuctionDetails
    fields = '__all__'
    success_url = reverse_lazy('showdetails_url')

class UpdateAuctionDetails(UpdateView):
    model = AuctionDetails
    fields = '__all__'
    success_url = reverse_lazy('showdetails_url')

class DeleteAuctionDetails(DeleteView):
    model = AuctionDetails
    fields = '__all__'
    success_url = reverse_lazy('showdetails_url')
    context_object_name = 'object_list'

#USER WISHLIST
class UserWishlistList(ListView):
    model = UserWishlist

class AddUserWishlist(CreateView):
    model = UserWishlist
    fields = '__all__'
    success_url = reverse_lazy('showwish_url')

class UpdateUserWishlist(UpdateView):
    model = UserWishlist
    fields = '__all__'
    success_url = reverse_lazy('showwish_url')

class DeleteUserWishlist(DeleteView):
    model = UserWishlist
    fields = '__all__'
    success_url = reverse_lazy('showwish_url')
    context_object_name = 'object_list'

#CURRENT AUCTION
class CurrentAuctionList(ListView):
    model = CurrentAuction

class AddCurrentAuction(CreateView):
    model = CurrentAuction
    fields = '__all__'
    success_url = reverse_lazy('showcurrent_url')

class UpdateCurrentAuction(UpdateView):
    model = CurrentAuction
    fields = '__all__'
    success_url = reverse_lazy('showcurrent_url')

class DeleteCurrentAuction(DeleteView):
    model = CurrentAuction
    fields = '__all__'
    success_url = reverse_lazy('showcurrent_url')
    context_object_name = 'object_list'

#BIDDER
class BidderList(ListView):
    model = Bidder

class AddBidder(CreateView):
    model = Bidder
    fields = '__all__'
    success_url = reverse_lazy('showbidder_url')

class UpdateBidder(UpdateView):
    model = Bidder
    fields = '__all__'
    success_url = reverse_lazy('showbidder_url')

class DeleteBidder(DeleteView):
    model = Bidder
    fields = '__all__'
    success_url = reverse_lazy('showbidder_url')
    context_object_name = 'object_list'

#AUTO BID
class AutoBidList(ListView):
    model = AutoBid

class AddAutoBid(CreateView):
    model = AutoBid
    fields = '__all__'
    success_url = reverse_lazy('showauto_url')

class UpdateAutoBid(UpdateView):
    model = AutoBid
    fields = '__all__'
    success_url = reverse_lazy('showauto_url')

class DeleteAutoBid(DeleteView):
    model = AutoBid
    fields = '__all__'
    success_url = reverse_lazy('showauto_url')
    context_object_name = 'object_list'

#SECURITY DEPOSITE
class SecurityDepositeList(ListView):
    model = SecurityDeposite

class AddSecurityDeposite(CreateView):
    model = SecurityDeposite
    fields = '__all__'
    success_url = reverse_lazy('showsecurity_url')

class UpdateSecurityDeposite(UpdateView):
    model = SecurityDeposite
    fields = '__all__'
    success_url = reverse_lazy('showsecurity_url')

class DeleteSecurityDeposite(DeleteView):
    model = SecurityDeposite
    fields = '__all__'
    success_url = reverse_lazy('showsecurity_url')
    context_object_name = 'object_list'

#CURRENT BID
class CurrentBidList(ListView):
    model = CurrentBid

class AddCurrentBid(CreateView):
    model = CurrentBid
    fields = '__all__'
    success_url = reverse_lazy('showcurrentbid_url')

class UpdateCurrentBid(UpdateView):
    model = CurrentBid
    fields = '__all__'
    success_url = reverse_lazy('showcurrentbid_url')

class DeleteCurrentBid(DeleteView):
    model = CurrentBid
    fields = '__all__'
    success_url = reverse_lazy('showcurrentbid_url')
    context_object_name = 'object_list'

#ALL BID
class AllBidList(ListView):
    model = AllBid

class AddAllBid(CreateView):
    model = AllBid
    fields = '__all__'
    success_url = reverse_lazy('showallbid_url')

class UpdateAllBid(UpdateView):
    model = AllBid
    fields = '__all__'
    success_url = reverse_lazy('showallbid_url')

class DeleteAllBid(DeleteView):
    model = AllBid
    fields = '__all__'
    success_url = reverse_lazy('showallbid_url')
    context_object_name = 'object_list'