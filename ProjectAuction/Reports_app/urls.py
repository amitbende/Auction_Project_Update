from django.urls import path
from . import views

urlpatterns = [
    path('sucf/', views.AddSuccessReport.as_view(), name = 'addsuccess_url'),
    path('sucl/', views.SuccessReportList.as_view(), name = 'showsuccess_url'),
    path('usuc/<int:pk>/', views.UpdateSuccessReport.as_view(), name = 'updatesuccess_url'),
    path('dsuc/<int:pk>/', views.DeleteSuccessReport.as_view(), name = 'deletesuccess_url'),

    path('canf/', views.AddCancelReport.as_view(), name = 'addcancel_url'),
    path('canl/', views.CancelReportList.as_view(), name = 'showcancel_url'),
    path('ucan/<int:pk>/', views.UpdateCancelReport.as_view(), name = 'updatecancel_url'),
    path('dcan/<int:pk>/', views.DeleteCancelReport.as_view(), name = 'deletecancel_url'),

    path('qf/', views.AddAuctionQuery.as_view(), name = 'addquery_url'),
    path('ql/', views.AuctionQueryList.as_view(), name = 'showquery_url'),
    path('uq/<int:pk>/', views.UpdateAuctionQuery.as_view(), name = 'updatequery_url'),
    path('dq/<int:pk>/', views.DeleteAuctionQuery.as_view(), name = 'deletequery_url'),

    path('fbf/', views.AddFeedBack.as_view(), name = 'addfeedback_url'),
    path('fbl/', views.FeedBackList.as_view(), name = 'showfeedback_url'),
    path('ufb/<int:pk>/', views.UpdateFeedBack.as_view(), name = 'updatefeedback_url'),
    path('dfb/<int:pk>/', views.DeleteFeedBack.as_view(), name = 'deletefeedback_url')

]