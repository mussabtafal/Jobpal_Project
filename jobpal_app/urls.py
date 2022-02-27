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
    path('companies/<int:company_id>', views.company_profile),
    path('company_jobs', views.company_jobs),
    path('company_jobs/<int:job_id>', views.applications),
    path('add_job', views.add_job),
    path('add_job/new', views.new),
    path('user_profile', views.user_profile),
]