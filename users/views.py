from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserResgistration
from tasks.models import Task


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
    tasks = Task.objects.filter(user_id=pk)
    context = {'tasks':tasks}
    return render(request, 'users/profile.html', context)