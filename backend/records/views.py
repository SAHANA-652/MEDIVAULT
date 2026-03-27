from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Patient


@require_GET
def health(request):
    return JsonResponse({"status": "ok", "patients": Patient.objects.count()})
