from django.urls import path

from .views import app_js, health, home, html_page, styles_css

urlpatterns = [
    path("", home, name="home"),
    path("health/", health),
    path("styles.css", styles_css, name="styles_css"),
    path("app.js", app_js, name="app_js"),
    path("<slug:page_name>.html", html_page, name="html_page"),
]
