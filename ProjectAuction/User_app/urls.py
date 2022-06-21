from django.urls import path
from . import views

urlpatterns = [
    path('cf/', views.AddCountry.as_view(), name = 'addcountry_url'),
    path('cl/', views.CountryList.as_view(), name = 'showcountry_url'),
    path('uc/<int:pk>/', views.UpdateCountry.as_view(), name = 'updatecountry_url'),
    path('dc/<int:pk>/', views.DeleteCountry.as_view(), name = 'deletecountry_url'),

    path('sf/', views.AddState.as_view(), name = 'addSState_url'),
    path('sl/', views.StateList.as_view(), name = 'showstate_url'),
    path('us/<int:pk>/', views.UpdateState.as_view(), name = 'updatestate_url'),
    path('ds/<int:pk>/', views.DeleteState.as_view(), name = 'deletestate_url'),

    path('cif/', views.AddCity.as_view(), name = 'addcity_url'),
    path('cil/', views.CityList.as_view(), name = 'showcity_url'),
    path('uci/<int:pk>/', views.UpdateCity.as_view(), name = 'updatecity_url'),
    path('dci/<int:pk>/', views.DeleteCity.as_view(), name = 'deletecity_url'),

    path('adf/', views.AddAddress.as_view(), name = 'addaddress_url'),
    path('adl/', views.AddressList.as_view(), name = 'showaddress_url'),
    path('uad/<int:pk>/', views.UpdateAddress.as_view(), name = 'updateaddress_url'),
    path('dad/<int:pk>/', views.DeleteAddress.as_view(), name = 'deleteaddress_url'),

    path('uf/', views.AddMyUser.as_view(), name = 'addmyuser_url'),
    path('ul/', views.MyUserList.as_view(), name = 'showmyuser_url'),
    path('uu/<int:pk>/', views.UpdateMyUser.as_view(), name = 'updatemyuser_url'),
    path('du/<int:pk>/', views.DeleteMyUser.as_view(), name = 'deletemyuser_url'),

    path('idf/', views.AddIdProof.as_view(), name = 'addidproof_url'),
    path('idl/', views.IdProofList.as_view(), name = 'showidproof_url'),
    path('uid/<int:pk>/', views.UpdateIdProof.as_view(), name = 'updateidproof_url'),
    path('did/<int:pk>/', views.DeleteIdProof.as_view(), name = 'deleteidproof_url'),

    path('hv/', views.Home_View, name='home_url')

]