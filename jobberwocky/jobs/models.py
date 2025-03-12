from django.db import models

# Create your models here.
class JobUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    salary_range_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_range_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    position_wanted = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
    class Meta:
        verbose_name = 'Job User'
        verbose_name_plural = 'Job Users'


class JobList(models.Model):
    position = models.CharField(max_length=200)
    skill = models.CharField(max_length=200, null=True, blank=True)

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    WORK_TYPE_CHOICES = [
        ('remote', 'Remote'),
        ('onsite', 'Onsite'),
        ('hybrid', 'Hybrid'),
    ]
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES)

    salary_range_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_range_max = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} {self.skill} - {self.city}, {self.country}"

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
