from django.contrib import admin
from django.urls import path
from .views import jobs_users_list_view, jobs_list_view, jobs_list_update_delete

urlpatterns = [
    path('jobsuser/', jobs_users_list_view, name="jobs_users_list_view"),
    path('joblist/', jobs_list_view, name='jobs_list_view'),
    path('joblist/<int:job_id>', jobs_list_update_delete, name='jobs_list_update_delete')
]
