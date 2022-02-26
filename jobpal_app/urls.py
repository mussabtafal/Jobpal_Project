from django.urls import path     
from . import views
urlpatterns = [
    path('', views.landing),
    path('about_us', views.about_us),
    path('jobs', views.jobs),
    path('jobs/1', views.job_detail),
    path('companies', views.companies),
    path('companies/1', views.company_profile),
    path('add_job', views.add_job),
    path('add_job/new', views.new),
]