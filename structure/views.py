from django.shortcuts import render
from structure.models import *
# Create your views here.
def listJobs(request):
	jobs = Job.objects.all()
	return render(request, 'viewJobs.html', {'jobs' : jobs})
	
def userProfile(request, target):
	user = User.objects.filter(UID=target)
	return render(request, 'userProfile.html', {'user' : user})

def companyProfile(request, target):
	company = Company.objects.filter(UID=target)
	return render(request, 'companyProfile.html', {'company' : company})

def viewJob(request, target):
	job = Job.objects.filter(UID=target)
	return render(request, 'viewJob.html', {'job' : job})
	
