from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserResgistration, UserUpdate, ProfileUpdate
from tasks.models import Task
from django.contrib.auth.models import User
from tasks.forms import AddTask
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView


def register(request):
    if request.method != 'POST':
        form = UserResgistration()
    else:
        form = UserResgistration(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect('users:login')

    context = {'form':form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request, pk):

    # Add a new task
    if request.method != 'POST':
        add_form = AddTask()
    else:
        add_form = AddTask(data=request.POST)
        if add_form.is_valid():
            task = Task(user=User.objects.get(id=pk), content=add_form.save(commit=False))
            task.save()
            return redirect('users:profile', request.user.id)

    tasks = Task.objects.filter(user_id=pk)
    context = {'tasks':tasks, 'add_form':add_form}
    return render(request, 'users/profile.html', context)


# Edit user profile
def edit_profile(request):

    if request.method != 'POST':
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)
    else:
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been successfully updated')
            return redirect('users:profile', request.user.id)

    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'users/edit_profile.html', context)


class PasswordReset(PasswordResetView):
    email_template_name = 'users/password_reset_email.html'
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:password_reset_done')

class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy('users:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'