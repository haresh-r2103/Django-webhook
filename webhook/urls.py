from django.urls import path
from .views import zoho_webhook

urlpatterns = [
    path("zoho/", zoho_webhook),
]