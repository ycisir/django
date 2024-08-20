from django.shortcuts import render, redirect
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group

# signup
def signup_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='Editor')
                user.groups.add(group)
                form = SignUpForm()
                messages.success(request, 'Account created successfully! login here')
                return redirect('login')

        else:
            form = SignUpForm()
    else:
        return redirect('profile')

    return render(request, 'enroll/signup.html', {'form':form})


# login
def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
    else:
        return redirect('profile')

    return render(request, 'enroll/login.html', {'form':form})


# profile
def profile_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(data=request.POST, instance=request.user)
                users = User.objects.all()
            else:
                form = EditUserProfileForm(request.POST, instance=request.user)
                users = None

            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated!')

        else:
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                form = EditUserProfileForm(instance=request.user)
                users = None

        return render(request, 'enroll/profile.html', {'name': request.user, 'form':form, 'users':users})
    
    else:
        return redirect('login')


# logout
def user_logout(request):
    logout(request)
    return redirect('login')


# change pass with old pass
# def change_pass_with_old(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PasswordChangeForm(user=request.user, data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 update_session_auth_hash(request, form.user)
#                 messages.success(request, 'Password changed successfully!')
#                 return redirect('profile')
#         else:
#             form = PasswordChangeForm(user=request.user)

#         return render(request, 'enroll/changepasswordwithold.html', {'form':form})
#     else:
#         return redirect('login')
    


# change pass without old pass
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully!')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)

        return render(request, 'enroll/changepassword.html', {'form':form})
    else:
        return redirect('login')



def user_details(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        form = EditAdminProfileForm(instance=user)
        return render(request, 'enroll/userdetails.html', {'form':form, 'user':user})
    else:
        return redirect('login')






