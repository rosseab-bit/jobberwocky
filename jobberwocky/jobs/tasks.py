# jobs/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import JobList, JobUser
from django.conf import settings

@shared_task
def send_job_email_notifications(job_id):
    job = JobList.objects.get(id=job_id)

    # Buscar usuarios que estén interesados en este puesto
    users = JobUser.objects.filter(position_wanted__icontains=job.position)

    for user in users:
        send_mail(
            subject=f"Nuevo trabajo disponible: {job.position}",
            message=f"Hola {user.first_name},\n\nTenemos una nueva oferta de trabajo para {job.position} en {job.city}, {job.country}. Si estás interesado, por favor verifica el anuncio.\n\nSaludos,\nPortal de Trabajos",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )

