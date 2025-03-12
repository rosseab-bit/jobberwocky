from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import JobUserSerializer, JobListSerializer, JobListCreateSerializer
from .models import JobUser, JobList
from .tasks import send_job_email_notifications
import requests
from .utils import format_data_api
# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of jobs with optional filtering",
    responses={200: JobUserSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new JobUser",
    responses={201: JobUserSerializer()},
    request_body=JobUserSerializer()
)
@api_view(['GET', 'POST'])
def jobs_users_list_view(request):
    if request.method == 'GET':
        users = JobUser.objects.all()
        serializer = JobUserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JobUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

position_param = openapi.Parameter('position', openapi.IN_QUERY, description="Filter by job position", type=openapi.TYPE_STRING, required=False)
work_type_param = openapi.Parameter('work_type', openapi.IN_QUERY, description="Filter by work type (e.g., remote, in-office)", type=openapi.TYPE_STRING, required=False)
@swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of jobs with optional filtering",
    responses={200: JobListSerializer(many=True)},
    manual_parameters=[position_param, work_type_param]
)
@swagger_auto_schema(
    method='post',
    operation_description="Create a new job listing",
    responses={201: JobListSerializer()},
    request_body=JobListCreateSerializer(),  
)
@api_view(['GET', 'POST'])
def jobs_list_view(request):
    if request.method == 'GET':
        url = 'http://localhost:8080/jobs'
        responseExternalData = requests.get(url)
        if responseExternalData.status_code == 200:
            api_data = responseExternalData.json()
        else:
            api_data = {}
        position = request.GET.get('position', None)
        work_type = request.GET.get('work_type', None)

        jobs = JobList.objects.all()
        if position:
            jobs = jobs.filter(position__icontains=position)
        if work_type:
            jobs = jobs.filter(work_type__icontains=work_type)

        serializer = JobListSerializer(jobs, many=True)
        join_data_api = serializer.data + format_data_api(api_data)
        return Response(join_data_api)
    elif request.method == 'POST':
        #serializer = JobListSerializer(data=request.data)
        serializer = JobListCreateSerializer(data=request.data)
        if serializer.is_valid():
            job = serializer.save()
            #send_job_email_notifications.delay(job.id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def jobs_list_update_delete(request, job_id=None):
    if request.method == 'PUT':
        if job_id is None:
            return Response({"detail": "Job ID is required to update."}, status=400)
        try:
            job = JobList.objects.get(id=job_id)
        except JobList.DoesNotExist:
            return Response({"detail": "Job not found."}, status=404)
        serializer = JobListCreateSerializer(job, data=request.data)
        if serializer.is_valid():
            job =  serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        try:
            job = JobList.objects.get(id=job_id)
        except JobList.DoesNotExist:
           return Response({"detail": "Job not found."}, status=404)
        
        job.delete()
        return Response({"detail": "Job deleted successfully."}, status=200)



