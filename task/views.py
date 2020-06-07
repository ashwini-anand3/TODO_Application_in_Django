from django.shortcuts import render,redirect
from .models import *
from .forms import TaskForm

# Create your views here.
def home(request):
	tasks=Task.objects.all()

	form = TaskForm()

	if request.method=='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	
	return render(request,'task/home.html',{'tasks':tasks,'form':form})

def update(request,id):
	task = Task.objects.get(id=id)

	form = TaskForm(instance=task)
	if request.method=='POST':
		form = TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request,'task/update.html',{'form':form})

def delete(request,id):
	task = Task.objects.get(id=id)
	if request.method=='POST':
		task.delete()
		return redirect('/')
	return render(request,'task/delete.html',{'task':task})