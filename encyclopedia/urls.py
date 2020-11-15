from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("random", views.randomPage, name="random"),
    path("<str:page>", views.wikiPage, name="wikiPage"),
    path("edit/<str:page>", views.editPage, name="edit")
]
