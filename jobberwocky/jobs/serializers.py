from rest_framework import serializers
from .models import JobUser, JobList

class JobUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobUser
        fields = ['id', 'first_name', 'last_name', 'email', 'salary_range_min', 'salary_range_max', 'position_wanted', 'created_at']


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = ['id', 'position', 'skill', 'country', 'city', 'work_type', 'salary_range_min', 'salary_range_max', 'created_at']

class JobListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = ['position', 'skill', 'country', 'city', 'work_type', 'salary_range_min', 'salary_range_max']
    def to_internal_value(self, data):
        if 'work_type' in data:
            data['work_type'] = data['work_type'].lower()
        return super().to_internal_value(data)
