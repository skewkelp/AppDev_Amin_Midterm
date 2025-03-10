from django.shortcuts import render, redirect
from datetime import datetime
# Used for converting input date (str) to datetime type
from django.utils import timezone
# Used to capture actual timezone for status logic
from . models import Tasks


def addTask(title, description, due_date):
# def addTask(title, description, due_date, status):
    check_datetime = datetime.strptime(due_date, '%Y-%m-%d').date()
    if check_datetime < timezone.now().date():
        status = "Overdue"
    # elif check_datetime == timezone.now().date():
    #     status = ""
    else:
        status = "Pending"


    item = Tasks(title=title, description=description, due_date=due_date, status=status)
    item.save()
    return


# Create your views here.
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        # status = request.POST.get('status')

        # addTask(title, description, due_date, status)
        addTask(title, description, due_date)
        return redirect('/task-manager/view-list')
    
    elif request.method == 'GET':
        return render(request, 'task_form.html')

def editTask(request, task):
    task.title = request.POST['title']
    task.description = request.POST['description']
    task.due_date = request.POST['due_date']
    task.status = request.POST['status']
    check_datetime = datetime.strptime(task.due_date, '%Y-%m-%d').date()

    if check_datetime < timezone.now().date():
        task.status = "Overdue"
    else:
        task.status = "Pending"

    task.save()
    return

def task_update(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == 'POST':
        editTask(request, task)
        return redirect('/task-manager/view-list')

    elif request.method == 'GET':
        return render(request, 'task_form.html', {'task': task})
   


def task_delete(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == 'POST':
        task = Tasks.objects.get(id=id)
        task.delete()
        return redirect('/task-manager/view-list')

    elif request.method == 'GET':
        return render(request,'task_confirm_delete.html', {'task': task})



# def index(request):
#     return render(request, 'index.html')

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def redirect_to_home(request):
    return redirect('task-manager/view-list')
