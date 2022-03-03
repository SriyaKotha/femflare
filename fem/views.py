from django.shortcuts import render
from fem.forms import RegistrationForm, ProfileForm


def home(request):
    return render(request, 'home.html')


def gallery(request):
    return render(request, 'gallery.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def register(request):
    form = RegistrationForm()
    userprofile = ProfileForm()
    return render(request=request, template_name="register.html",
                  context={"register_form": form, 'userprofileform': userprofile})


def register_success(request):
    return render(request, 'Registration_Success.html')

