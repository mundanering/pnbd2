from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Konto {username} zostało pomyślnie założone!")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})

    @login_required
    def profile(request):
        return render(request, 'users/profile.html')