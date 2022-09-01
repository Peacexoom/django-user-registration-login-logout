from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# priyanshu password:harry$$$***

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')  

def logoutUser(request):
    logout(request)
    return redirect("/login") 

def signupUser(request):
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         return redirect("/")

    # else:
    #     form = UserCreationForm()

    # return render(request, 'signup.html',{
    #     'form':form,
    # })

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form = User.objects.create_user(username, email, password)
        form.save()

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")

    else:
        return render(request, 'signup.html')

    return render(request, 'signup.html')

        
