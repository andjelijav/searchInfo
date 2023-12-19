from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import(
    LoginForm,
    RegistrationForm,
)


# Create your views here.
def home(request):
    return render(request,"main.html")

#@breaf Login page view render function
#@param request

def loginView(request):
    
    if request.method == "POST":
         #create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
         #check whether it's valid:
        if form.is_valid():
             #process the data in form.cleaned_data as required
             #...
             #redirect to a new URL:
            return HttpResponseRedirect("")
            #print()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    
    context = {"form": form}

    return render(request, "login.html", context)

#@breaf Registration page view render function
#@param request
def registrationView(request):
    
    if request.method == "GET":
         #create a form instance and populate it with data from the request:
        formR = RegistrationForm(request.GET)
         #check whether it's valid:
        if formR.is_valid():
             #process the data in form.cleaned_data as required
             #...
             #redirect to a new URL:
            return HttpResponseRedirect("")
            #print()

    # if a GET (or any other method) we'll create a blank form
    else:
        formR = RegistrationForm()
    
    context = {"form": formR}

    return render(request, "registration.html", context)