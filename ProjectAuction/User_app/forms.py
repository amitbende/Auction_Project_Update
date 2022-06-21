from django import forms
from .models import *

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.none()

        if 'country' in self.data:
            try:
                state_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(state_id=state_id).order_by('state_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.college.branch_set.order_by('state_name')

        elif 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = State.objects.filter(city_id=state_id).order_by('city_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.college.branch_set.order_by('city_name')
'''

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'

class IdProofForm(forms.ModelForm):
    class Meta:
        model = IdProof
        fields = '__all__'