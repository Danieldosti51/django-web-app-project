from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Job


# Create your views here.
def home(request):
    jobs = Job.objects.all().order_by("-pk")
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})
