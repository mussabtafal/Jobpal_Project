from django.shortcuts import render,redirect
from .models import User, Company,Job
from django.contrib import messages

def landing(request):
    return render (request, 'landing.html')

def about_us(request):
    return render (request, 'about_us.html')

def jobs(request):
    return render (request, 'job_list.html')

def job_detail(request):
    return render (request, 'job_detail.html')

def companies(request):
    return render (request, 'company_list.html')

def company_profile(request):
    return render (request, 'company_profile.html')

def add_job(request):
    return render (request, 'add_job.html')

def new (request):
    errors = Job.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add_job')
    else:
        this_company= Company.objects.get(id=request.session['company_id'] )
        Job.objects.create(title=request.POST['title'],location=request.POST['location'],
        desc=request.POST['desc'],category=request.POST['category'],company_job=this_company)
        messages.success(request, "Job successfully added")
        return redirect('/add_job')

