from django.http import HttpResponse
from django.shortcuts import render, redirect


from.models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'obj1'

class Taskdetailview(DetailView)  :
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('heading','author','date','blog')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('task')


def task_view(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        author = request.POST.get('author')
        date=request.POST.get('date')
        blog = request.POST.get('blog')


        obj = Task(heading=heading,author=author,date=date,blog=blog,)
        obj.save()
    obj1=Task.objects.all()
    return render(request,"index.html", {'obj1': obj1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render (request,'delete.html',{'task':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})