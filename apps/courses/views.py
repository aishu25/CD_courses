from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from django.contrib import messages
# Create your views here.

def index(request):
	print "******************"
	print "inside index"
	context = {
				"courses" : Course.objects.order_by('created_at')
				}

	return render(request,'courses/index.html',context)


def add(request):
	print "******************"
	print "inside add"
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		Course.objects.create(course_name=request.POST.get('course_name'),desc= request.POST.get('desc'))
		print "################"
		print "inside create"
		return redirect('/')
def confirm(request,id):
	context = {
				"courses" : Course.objects.get(id=id),
				}

	return render(request,'courses/delete.html',context)
def delete(request,id):

	Course.objects.get(id=id).delete()
	return redirect('/')
