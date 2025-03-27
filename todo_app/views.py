from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Category
from .forms import TaskForm, CategoryForm, UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'帳號 {username} 已建立成功！請登入')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'todo_app/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    categories = Category.objects.all()
    
    # 過濾
    category_id = request.GET.get('category')
    priority = request.GET.get('priority')
    completed = request.GET.get('completed')
    
    if category_id:
        tasks = tasks.filter(category__id=category_id)
    if priority:
        tasks = tasks.filter(priority=priority)
    if completed:
        is_completed = completed == 'True'
        tasks = tasks.filter(completed=is_completed)
    
    return render(request, 'todo_app/task_list.html', {
        'tasks': tasks,
        'categories': categories
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, '任務已新增！')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo_app/task_form.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, '任務已更新！')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/task_form.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, '任務已刪除！')
        return redirect('task_list')
    return render(request, 'todo_app/task_confirm_delete.html', {'task': task})

@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '類別已新增！')
            return redirect('task_list')
    else:
        form = CategoryForm()
    return render(request, 'todo_app/category_form.html', {'form': form})
