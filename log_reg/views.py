from django.shortcuts import render,redirect
from .models import User, Company
import bcrypt
from django.contrib import messages

def user_register(request):
    return render (request, 'users_register.html')

def add_new_user (request):
    request.session['coming_from']="REGISTER"
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user_register')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],
        email=request.POST['email'],password=pw_hash,birthday=request.POST['birthday'])
        messages.success(request, "User successfully registered")
        return redirect('/user_register')

def user_login(request):
    errors = User.objects.basic_validator_second(request.POST)
    request.session['coming_from']="LOGIN"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user_register')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/')
            else:
                request.session['error1']=str('Wrong password')
                print('wrong password')
                return redirect('/user_register')


def company_register(request):
    return render (request, 'company_register.html')

def add_new_company (request):
    request.session['coming_from']="REGISTER"
    errors = Company.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/company_register')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        Company.objects.create(company_name=request.POST['company_name'],location=request.POST['location'],desc=request.POST['desc'],
        email=request.POST['email'],password=pw_hash)
        messages.success(request, "Company successfully registered")
        return redirect('/company_register')

def company_login(request):
    request.session['coming_from']="LOGIN"
    errors = Company.objects.basic_validator_second(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/company_register')
    else:
        company = Company.objects.filter(email=request.POST['email'])
        if company: 
            logged_company = company[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_company.password.encode()):
                request.session['company_id'] = logged_company.id
                return redirect('/')
            else:
                request.session['error1']=str('Wrong password')
                print('wrong password')
                return redirect('/company_register')


# Create your views here.
