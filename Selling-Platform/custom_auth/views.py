from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm, LoginForm


User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        return redirect('product_list_initial')
    return redirect('login')


def registeration(request):
    if request.user.is_authenticated:
        return redirect('product_list_initial')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('product_list_initial')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("product_list_initial")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    form = LoginForm()
    return render(request=request, template_name="login.html", context={"form": form})


def custom_logout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("login")
