from django.shortcuts import render

from .models import Video
from referals.models import Partner


def index(request):
    partner = None
    utm = request.GET.get("utm", None)
    if utm:
        if Partner.objects.filter(utm=utm).exists():
            partner = Partner.objects.filter(utm=utm)[0]

    videos = Video.objects.all()
    return render(
        request, "videos/index.html", context={"videos": videos, "partner": partner}
    )
