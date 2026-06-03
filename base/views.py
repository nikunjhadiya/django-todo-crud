from base.models import TaskModel, CompleteModel, TrashModel
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request, 'home.html', {'data': data})

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        TaskModel.objects.create(
            title=title,
            description=description
        )

        return redirect("home")
    return render(request, "add.html")


def delete(request, pk):
    data = TaskModel.objects.get(id=pk)

    TrashModel.objects.create(
        title=data.title,
        description=data.description
    )

    data.delete()
    return redirect('home')


def update(request, pk):
    data = TaskModel.objects.get(id=pk)

    if request.method == "POST":
        data.title = request.POST['title']
        data.description = request.POST['description']
        data.save()
        return redirect('home')
    return render(request, 'update.html', {'data': data})

        
def completed(request):
    data = CompleteModel.objects.all()
    return render(request, 'completed.html', {'data': data})

def complete(request, pk):
    data = TaskModel.objects.get(id=pk)
    CompleteModel.objects.create(
        title=data.title,
        description=data.description
    )
    data.delete()
    return redirect('home')

def completeall(request):
    data = TaskModel.objects.all()
    for i in data:
        CompleteModel.objects.create(
        title=i.title,
        description=i.description
        )
        i.delete()
    return redirect('home')    

def deleteall(request):
    data = TaskModel.objects.all()
    for i in data:
        TrashModel.objects.create(
        title=i.title,
        description=i.description
        )
        i.delete()
    return redirect('home')

def crestore(request, pk):
    data = CompleteModel.objects.get(id=pk)

    TaskModel.objects.create(
        title=data.title,
        description=data.description
    )

    data.delete()
    return redirect('home')

def cdelete(request, pk):
    data = CompleteModel.objects.get(id=pk)

    TrashModel.objects.create(
        title=data.title,
        description=data.description
    )

    data.delete()
    return redirect('completed')

def trestore(request, pk):
    data = TrashModel.objects.get(id=pk)

    TaskModel.objects.create(
        title=data.title,
        description=data.description
    )

    data.delete()
    return redirect('home')

def tdelete(request, pk):
    TrashModel.objects.get(id=pk).delete()
    return redirect('trash')

def trestoreall(request):
    data = CompleteModel.objects.all()

    for task in data:
        TaskModel.objects.create(
            title=task.title,
            description=task.description
        )
        task.delete()
    return redirect('completed')

def tdeleteall(request):
    data = CompleteModel.objects.all()

    for task in data:
        TrashModel.objects.create(
            title=task.title,
            description=task.description
        )
        task.delete()
    return redirect('completed')
        
def trashrestoreall(request):
    data = TrashModel.objects.all()

    for task in data:
        TaskModel.objects.create(
            title=task.title,
            description=task.description
        )
        task.delete()

    return redirect('trash')


def trashdeleteall(request):
    TrashModel.objects.all().delete()
    return redirect('trash')
        
def trash(request):
    data = TrashModel.objects.all()
    return render(request, 'trash.html', {'data': data})

def about(request):
    return render(request,'about.html')