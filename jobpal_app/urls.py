from django.urls import path     
from . import views
urlpatterns = [
    path('', views.landing),
    path('about_us', views.about_us),
    path('jobs', views.jobs),
    path('jobs/filter_category', views.f_category),
    path('jobs/filteredJobs', views.render_category),
    path('jobs/<int:job_id>', views.job_detail),
    path('jobs/<int:job_id>/apply', views.job_apply),
    path('companies', views.companies),
    path('companies/1', views.company_profile),
    path('add_job', views.add_job),
    path('add_job/new', views.new),
]