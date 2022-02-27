from django.shortcuts import render,redirect
from .models import User, Company,Job
from django.contrib import messages
from django.http import JsonResponse

def landing(request):
    all_jobs = Job.objects.all()
    context = {
        "jobs": all_jobs,
    }
    return render (request, 'landing.html', context)

def about_us(request):
    return render (request, 'about_us.html')

def jobs(request):
    if "term" in request.GET:
        search = Job.objects.filter(title__contains = request.GET.get('term'))
        titles = []
        for job in search:
            titles.append(job.title)
        return JsonResponse(titles, safe=False)
    all_jobs = Job.objects.all()
    all_companies = Company.objects.all()
    context = {
        "jobs": all_jobs,
        "companies": all_companies
    }
    return render (request, 'job_list.html', context)

def search (request):
    searched_jobs = Job.objects.filter(title__contains = request.GET['search_bar'])
    all_companies = Company.objects.all()
    all_jobs = Job.objects.all()
    context = {
        "searched_jobs": searched_jobs,
        "jobs": all_jobs,
        "companies": all_companies
    }
    return render (request,'job_search.html', context)

def job_detail(request, job_id):
    this_job = Job.objects.get(id = job_id)
    all_jobs = Job.objects.all()
    context = {
        "job": this_job,
        "jobs": all_jobs
    } 
    return render (request, 'job_detail.html', context)

def f_category(request):
    if 'f_category' in request.POST:
        if request.POST['f_category'] == "":
            return redirect("/jobs")
        if 'f_company' in request.session:
            del request.session['f_company']
        request.session['f_category'] = request.POST['f_category']
        return redirect("/jobs/filteredJobs")
    else:
        if request.POST['f_company'] == "":
                return redirect("/jobs")
        if 'f_category' in request.session:
            del request.session['f_category']
        request.session['f_company'] = request.POST['f_company']
        return redirect("/jobs/filteredJobs")

def render_category(request):
    if 'f_category' in request.session:
        cat_filter = Job.objects.filter(category = request.session['f_category'])
        all_jobs = Job.objects.all()
        all_companies = Company.objects.all()
        context = {
            "filteredJobs": cat_filter,
            "jobs": all_jobs,
            "companies": all_companies
        }
        return render(request, "job_list_filter.html", context)
    else:
        this_company = Company.objects.get(company_name = request.session['f_company'])
        com_filter = Job.objects.filter(company_job = this_company)
        print(com_filter)
        print("*"*200)
        all_jobs = Job.objects.all()
        all_companies = Company.objects.all()
        context = {
            "filteredJobs": com_filter,
            "jobs": all_jobs,
            "companies": all_companies
        } 
        return render(request, "job_list_filter.html", context)

def job_apply(request, job_id):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        this_job = Job.objects.get(id = job_id)
        this_user = User.objects.get(id = request.session['user_id'])
        all_appliers = this_job.user_job.all()
        if this_user in all_appliers:
            messages.success(request,"Already Applied")
            return redirect('/user_profile')
        else:
            this_job.user_job.add(this_user)
            messages.success(request,"Successfully Applied")
            return redirect('/user_profile')

def companies(request):
    context={
        'all_companies':Company.objects.all()
    }
    return render (request, 'company_list.html',context)

def company_jobs(request):
    this_company=Company.objects.get(id = request.session['company_id'])
    context={
        'all_jobs':Job.objects.filter(company_job=this_company),
        'this_company':this_company
    }
    return render (request,'company_added_jobs.html',context)

def applications(request, job_id):
    company_job=Job.objects.get(id = job_id)
    context={
        'all_users':User.objects.filter(jobs = company_job)
    }
    return render (request,'applications.html',context)

def company_profile(request,company_id):
    this_company= Company.objects.get(id=company_id)
    context={
        'company':this_company,
        'all_companies':Company.objects.all()
    }
    return render (request, 'company_profile.html',context)

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

def user_profile(request):
    this_user = User.objects.get(id = request.session['user_id'])
    user_jobs = Job.objects.filter(user_job = this_user)
    context={
        'user_jobs':user_jobs,
        'this_user': this_user
    }
    return render (request, 'user_profile.html',context)

def delete_job(request, job_id):
    this_job = Job.objects.get(id = job_id)
    this_job.delete()
    return redirect('/company_jobs')