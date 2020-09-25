from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            message = messages.success(request, f"User {username} has been created successfully")
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {"form": form})


def profile(request):
    return render(request, "accounts/profile.html")


# class RegisterView(View):
#     def get(self, request):
#         form = UserRegister
#         return render(request, 'accounts/register.html', {"form": form})
#
#     def post(self, request):
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             form.save()
#             message = messages.success(request, f"User {username} created successfully")
#             return redirect("home")
#         return render(request, 'accounts/register.html', {"form": form})
