from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

def login(request):
	return render(request, 'users/login.html')

def logout(request):
	return render(request, 'users/logout.html')

#@csrf_exempt
@login_required
def profile(request):

	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated')
			return redirect('users-profile')

	else:
#		messages.error(request, request.method)
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)




def register(request):
#	form = UserCreationForm()
#	return render(request, 'users/register.html', {'form':form})

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('webapp-home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def forgot_password(request):
	return render(request, 'users/forgot_password.html')

def user_list(request):
	users = User.objects.all()
	return render(request, 'users/user_list.html', {'users':users})






























