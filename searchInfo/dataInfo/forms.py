from django import forms

#@breaf login form.
#@param forms.Form > Base class for form.
class LoginForm(forms.Form):

    your_username = forms.CharField(label="Your username", max_length=100,required=False)
    
    your_password=forms.CharField(label="Your password", max_length=50,required=False )