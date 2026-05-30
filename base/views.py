from django.shortcuts import render
from base.models import TaskModel
from django.shortcuts import render,redirect



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
    TaskModel.objects.get(id=pk).delete()
    return redirect(home)


def update(request, pk):
    data = TaskModel.objects.get(id=pk)

    if request.method == "POST":
        data.title = request.POST['title']
        data.description = request.POST['description']

        data.save()

        return redirect(home)

    return render(request, 'update.html', {'data': data})

        
def completed(request):
    return render(request,'completed.html')

def trash(request):
    return render(request,'trash.html')

def about(request):
    return render(request,'about.html')
