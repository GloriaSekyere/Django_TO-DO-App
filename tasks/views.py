from django.shortcuts import render, redirect
from .models import Task 
from .forms import AddTask


# Homepage 
def index(request):
    return render(request, 'tasks/index.html')

# Edit an existing task
def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method != 'POST':
        edit_form = AddTask(instance=task)
    else:
        edit_form = AddTask(instance=task, data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('users:profile', request.user.id)
    
    context = {'task':task, 'edit_form':edit_form}
    return render(request, 'tasks/edit_task.html', context)

# Delete a task
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('users:profile', request.user.id)
    