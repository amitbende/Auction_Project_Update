from django.urls import path
from . import views

urlpatterns = [
    path('adf/', views.AddAuctionDetails.as_view(), name = 'adddetails_url'),
    path('adl/', views.AuctionDetailsList.as_view(), name = 'showdetails_url'),
    path('uad/<int:pk>/', views.UpdateAuctionDetails.as_view(), name = 'updatedetails_url'),
    path('dad/<int:pk>/', views.DeleteAuctionDetails.as_view(), name = 'deletedetails_url'),

    path('uwf/', views.AddUserWishlist.as_view(), name = 'addwishlist_url'),
    path('uwl/', views.UserWishlistList.as_view(), name = 'showwishlist_url'),
    path('uuw/<int:pk>/', views.UpdateUserWishlist.as_view(), name = 'updatewishlist_url'),
    path('duw/<int:pk>/', views.DeleteUserWishlist.as_view(), name = 'deletewishlist_url'),

    path('caf/', views.AddCurrentAuction.as_view(), name = 'addcurrent_url'),
    path('cal/', views.CurrentAuctionList.as_view(), name = 'showcurrent_url'),
    path('uca/<int:pk>/', views.UpdateCurrentAuction.as_view(), name = 'updatecurrent_url'),
    path('dca/<int:pk>/', views.DeleteCurrentAuction.as_view(), name = 'deletecurrent_url'),

    path('bf/', views.AddBidder.as_view(), name = 'addbidder_url'),
    path('bl/', views.BidderList.as_view(), name = 'showbidder_url'),
    path('ub/<int:pk>/', views.UpdateBidder.as_view(), name = 'updatebidder_url'),
    path('db/<int:pk>/', views.DeleteBidder.as_view(), name = 'deletebidder_url'),

    path('abf/', views.AddAutoBid.as_view(), name = 'addauto_url'),
    path('abl/', views.AutoBidList.as_view(), name = 'showauto_url'),
    path('uab/<int:pk>/', views.UpdateAutoBid.as_view(), name = 'updateauto_url'),
    path('dab/<int:pk>/', views.DeleteAutoBid.as_view(), name = 'deleteauto_url'),

    path('sdf/', views.AddSecurityDeposite.as_view(), name = 'addsecurity_url'),
    path('sdl/', views.SecurityDepositeList.as_view(), name = 'showsecurity_url'),
    path('usd/<int:pk>/', views.UpdateSecurityDeposite.as_view(), name = 'updatesecurity_url'),
    path('dsd/<int:pk>/', views.DeleteSecurityDeposite.as_view(), name = 'deletesecurity_url'),

    path('cbf/', views.AddCurrentBid.as_view(), name = 'addcurrentbid_url'),
    path('cbl/', views.CurrentBidList.as_view(), name = 'showcurrentbid_url'),
    path('ucb/<int:pk>/', views.UpdateCurrentBid.as_view(), name = 'updatecurrentbid_url'),
    path('dcb/<int:pk>/', views.DeleteCurrentBid.as_view(), name = 'deletecurrentbid_url'),

    path('abf/', views.AddAllBid.as_view(), name = 'addallbid_url'),
    path('abl/', views.AllBidList.as_view(), name = 'showallbid_url'),
    path('uab/<int:pk>/', views.UpdateAllBid.as_view(), name = 'updateallbid_url'),
    path('dab/<int:pk>/', views.DeleteAllBid.as_view(), name = 'deleteallbid_url')

]