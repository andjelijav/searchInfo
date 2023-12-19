from django import forms

#@breaf login form.
#@param forms.Form > Base class for form.
class LoginForm(forms.Form):

    email = forms.CharField(label="email ", max_length=50)
    
    password=forms.CharField(label="password", max_length=50 )

#@breaf registration form
#@param forms.Form > Base class for form.
class RegistrationForm(forms.Form):
    your_email =forms.EmailField(label="Your email address", max_length=100)
    your_username= forms.CharField(label="Your username", max_length=50)
    your_password=forms.CharField(label="Your password", max_length=50)
    password_conformation=forms.CharField(label="Password conformation", max_length=50)
    your_name=forms.CharField(label='Your name', max_length=50)
    your_last_name=forms.CharField(label='Your lastname', max_length=50)

    
