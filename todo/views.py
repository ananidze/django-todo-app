from django.shortcuts import render, redirect

from todo.models import Todo


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title != '':
            Todo.objects.create(title=title)
        return redirect('home')
    data = Todo.objects.all()
    return render(request, 'home.html', context={'data': data})


def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('home')


def complete(request, id):
    data = Todo.objects.get(id=id)
    data.is_completed = True
    data.save()
    return redirect('home')


def incomplete(request, id):
    data = Todo.objects.get(id=id)
    data.is_completed = False
    data.save()
    return redirect('home')
