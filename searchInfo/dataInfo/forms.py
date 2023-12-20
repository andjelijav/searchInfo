from django import forms

#@breaf login form.
#@param forms.Form > Base class for form.
class LoginForm(forms.Form):

    email = forms.CharField(label="email ", max_length=50)
    
    password=forms.CharField(label="password", max_length=50 )

#@breaf registration form
#@param forms.Form > Base class for form.
class RegistrationForm(forms.Form):
    email =forms.EmailField(label="Your email address", max_length=100)
    
    password=forms.CharField(label="Your password", max_length=50)
    
    first_name=forms.CharField(label='Your name', max_length=50)
    last_name=forms.CharField(label='Your lastname', max_length=50)

    
