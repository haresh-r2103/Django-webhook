from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

def health_check(request):
    return JsonResponse({
        "status": "running",
        "service": "Ticket AI Backend"
    })

urlpatterns = [
    path("", health_check),
    path("admin/", admin.site.urls),
    path("api/webhooks/", include("webhook.urls")),
]