from django import forms
from .models import Twik
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#django forms structure
class Twikform(forms.ModelForm):
    class Meta:
        model=Twik
        fields=['text','photo']

class RegisForm(UserCreationForm):
    email=forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields=('username','email','password1','password2')#due to django orm, internal security purposes... mandetory syntax