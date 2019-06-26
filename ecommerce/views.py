from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    context = {
        "title":"Home page",
        "content":"Welcome to Home page"
    }

    if request.user.is_authenticated:
        context["premium_content"] = "YEAHH You are logged in"
        
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
        "title":"About page",
        "content":"Welcome to About page"
    }
    return render(request,"home_page.html",context)


def contact_page(request):
    contact_form_obj = ContactForm(request.POST or None)
    context = {
        "title":"Contact page",
        "content":"Welcome to Contact page",
        "form":contact_form_obj
    }
    if contact_form_obj.is_valid():
        print(contact_form_obj.cleaned_data)
        contact_form_obj

    return render(request,"contact/view.html",context)


def login_page(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }
    # print(request.user.is_authenticated)
    context = {
        "form":form
    }
    if form.is_valid():
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print("user ", user)
        if user is not None:
            login(request, user)
            
            return redirect("/login")

    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        print(form.cleaned_data)

    return render(request, "auth/register.html", context)