from django import forms
from app.models import *
class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']