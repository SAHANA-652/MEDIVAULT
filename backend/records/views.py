from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.views.decorators.http import require_GET

from .models import Patient


def home(request):
    return render(request, "records/index.html")


def html_page(request, page_name: str):
    """
    Serve your existing frontend HTML files from `templates/records/`.
    Example: /login.html -> records/login.html
    """
    try:
        return render(request, f"records/{page_name}.html")
    except TemplateDoesNotExist as e:
        raise Http404(str(e))


def styles_css(request):
    css_path = settings.BASE_DIR / "static" / "css" / "styles.css"
    try:
        return FileResponse(open(css_path, "rb"), content_type="text/css")
    except FileNotFoundError:
        raise Http404("styles.css not found")


def app_js(request):
    js_path = settings.BASE_DIR / "static" / "js" / "app.js"
    try:
        return FileResponse(open(js_path, "rb"), content_type="application/javascript")
    except FileNotFoundError:
        raise Http404("app.js not found")


@require_GET
def health(request):
    return JsonResponse({"status": "ok", "patients": Patient.objects.count()})
