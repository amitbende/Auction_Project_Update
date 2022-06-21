from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
#COUNTRY
class CountryList(ListView):
    model = Country

class AddCountry(CreateView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('showcountry_url')

class UpdateCountry(UpdateView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('showcountry_url')

class DeleteCountry(DeleteView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('showcountry_url')
    context_object_name = 'object_list'


#STATE
class StateList(ListView):
    model = State

class AddState(CreateView):
    model = State
    fields = '__all__'
    success_url = reverse_lazy('showstate_url')

class UpdateState(UpdateView):
    model = State
    fields = '__all__'
    success_url = reverse_lazy('showstate_url')

class DeleteState(DeleteView):
    model = State
    fields = '__all__'
    success_url = reverse_lazy('showstate_url')
    context_object_name = 'object_list'

#CITY
class CityList(ListView):
    model = City

class AddCity(CreateView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('showcity_url')

class UpdateCity(UpdateView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('showcity_url')

class DeleteCity(DeleteView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('showcity_url')
    context_object_name = 'object_list'

#ADDRESS
class AddressList(ListView):
    model = Address

class AddAddress(CreateView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('showaddress_url')

class UpdateAddress(UpdateView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('showaddress_url')

class DeleteAddress(DeleteView):
    model = Address
    fields = '__all__'
    success_url = reverse_lazy('showaddress_url')
    context_object_name = 'object_list'

#USER
class MyUserList(ListView):
    model = MyUser

class AddMyUser(CreateView):
    model = MyUser
    fields = '__all__'
    success_url = reverse_lazy('showmyuser_url')

class UpdateMyUser(UpdateView):
    model = MyUser
    fields = '__all__'
    success_url = reverse_lazy('showmyuser_url')

class DeleteMyUser(DeleteView):
    model = MyUser
    fields = '__all__'
    success_url = reverse_lazy('showmyuser_url')
    context_object_name = 'object_list'

#ID-PROOF
class IdProofList(ListView):
    model = IdProof

class AddIdProof(CreateView):
    model = IdProof
    fields = '__all__'
    success_url = reverse_lazy('showidproof_url')

class UpdateIdProof(UpdateView):
    model = IdProof
    fields = '__all__'
    success_url = reverse_lazy('showidproof_url')

class DeleteIdProof(DeleteView):
    model = IdProof
    fields = '__all__'
    paginate_by = 2
    success_url = reverse_lazy('showidproof_url')
    context_object_name = 'object_list'

def Home_View(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)
