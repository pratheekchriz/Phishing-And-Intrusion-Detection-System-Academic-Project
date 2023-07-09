from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		
	def __init__(self, *args, **kwargs):
         super(NewUserForm, self).__init__(*args, **kwargs)
         self.fields['username'].widget.attrs.update({'class': 'form-control'}),
         self.fields['email'].widget.attrs.update({'class': 'form-control'}),
         self.fields['password1'].widget.attrs.update({'class': 'form-control'}),
         self.fields['password2'].widget.attrs.update({'class': 'form-control'}),

def save(self, commit=True):
    user = super(NewUserForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user

