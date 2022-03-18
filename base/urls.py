from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("veille", views.veille, name='veille'),
    path("details/<int:id>", views.article_details, name='article_details'),
    path("stage", views.stage_page, name="stage_page"),
    path("cv_page", views.cv_page, name="cv_page"),
]
