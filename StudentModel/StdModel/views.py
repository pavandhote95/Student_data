from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import StudentModel

def home(req):
	return render(req,'index.html')

def add(req):
	return render(req,'add.html')

def addTask(req):
	ob=StudentModel()
	ob.rno=req.GET.get('rno')
	ob.name=req.GET.get('name')
	ob.marks=req.GET.get('marks')
	#ob.date=req.GET.get('date')
	ob.save()
	return render(req,'show.html')

def delete(req):
	pid=req.GET.get('pid')
	ob=StudentModel.objects.get(id=pid)
	ob.delete()
	return redirect("/show")

def update(req):
	if req.method=='GET':
		pid=req.GET.get('pid')
		ob=StudentModel.objects.get(id=pid)
		return render(req,"update.html",{'rec':ob})
	else:
		ob=StudentModel()
		ob.id=req.POST.get('pid')
		ob.rno=req.POST.get('rno')
		ob.name=req.POST.get('name')
		ob.marks=req.POST.get('marks')
		ob.save()
		return redirect("/show")


def show(req):
	ob=StudentModel.objects.all()
	return render(req,'show.html',{'ob':ob})


# Create your views here.
