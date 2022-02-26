from django.db import models
import re
from datetime import datetime


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first_name should be at least 2 characters"
        name_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not name_REGEX.match(postData['first_name']):               
            errors['first_name'] = "first_name should be letters only"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last_name should be at least 2 characters"
        if not name_REGEX.match(postData['last_name']):               
            errors['last_name'] = "last_name should be letters only"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        email_validate = User.objects.filter(email=postData['email'])
        if len(email_validate) > 0 :
            errors['val_email'] = "email already exists"
        if len(postData['password']) < 8 :
            errors["password"] = "password should be at least 8 characters"
        if  postData['password'] != postData['password_con']:
            errors["password"] = "Password dose not match confirm PW"
        if  postData['birthday'] > str(datetime.now()) :
            errors["birthday"] = "Birthday should be in the past"
        if  postData['birthday'] > str(datetime(2011,1,1)):
            errors["age"] = "Users should be at least 13 years old"
        return errors
    
    def basic_validator_second(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        email_validate = User.objects.filter(email=postData['email'])
        if not email_validate :
            errors['val_email'] = "register first"
        if len(postData['password']) < 8 :
            errors["password"] = "password should be at least 8 characters"
        return errors



class CompanyManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['company_name']) < 2:
            errors["company_name"] = "Company name should be at least 2 characters"
        if len(postData['location']) < 5:
            errors["location"] = "location should be at least 5 characters"
        if len(postData['desc']) < 20:
            errors["desc"] = "Description should be at least 20 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        email_validate = Company.objects.filter(email=postData['email'])
        if len(email_validate) > 0 :
            errors['val_email'] = "email already exists"
        if len(postData['password']) < 8 :
            errors["password"] = "password should be at least 8 characters"
        if  postData['password'] != postData['password_con']:
            errors["password"] = "Password dose not match confirm PW"
        return errors
    
    def basic_validator_second(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        email_validate = Company.objects.filter(email=postData['email'])
        if not email_validate :
            errors['val_email'] = "register first"
        if len(postData['password']) < 8 :
            errors["password"] = "password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=90)
    last_name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    birthday=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Company(models.Model):
    company_name=models.CharField(max_length=90)
    location=models.CharField(max_length=90)
    desc=models.TextField()
    email=models.CharField(max_length=90)
    category=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CompanyManager()

# Create your models here.
