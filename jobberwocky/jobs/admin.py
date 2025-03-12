from django.contrib import admin
from .models import JobUser, JobList

# Register your models here.
class JobUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position_wanted', 'salary_range_min', 'salary_range_max', 'created_at')
    list_filter = ('position_wanted', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'position_wanted')


class JobAdmin(admin.ModelAdmin):
    list_display = ('position', 'skill', 'city', 'country', 'work_type', 'salary_range_min', 'salary_range_max', 'created_at')
    list_filter = ('work_type', 'country', 'created_at')
    search_fields = ('position', 'country', 'city')

admin.site.register(JobList, JobAdmin)
admin.site.register(JobUser, JobUserAdmin)
