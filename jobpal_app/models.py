from django.db import models
from log_reg.models import User , Company


class JobManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors["title"] = "title should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Description should be at least 15 characters"
        if len(postData['location']) < 5:
            errors["location"] = "location should be at least 5 characters"
        if postData['category'] == 'Category':
            errors["category"] = "category should be entered"
        return errors


class Job(models.Model):
    title=models.CharField(max_length=90)
    desc=models.TextField()
    location=models.CharField(max_length=95)
    category=models.CharField(max_length=90)
    user_job = models.ManyToManyField(User, related_name="jobs")
    company_job=models.ForeignKey(Company, related_name="add_job", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()


