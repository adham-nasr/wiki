from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index") ,
    path("wiki/<str:page_name>/", views.get_page, name="get_page") ,
    path("random/", views.random , name="random") ,
    path("search/", views.search , name="search") ,
    path("create/" ,views.create , name="create") ,
    path("error/<str:error_message>/" , views.error , name="error") ,
    path("edit/<str:title>/" , views.edit , name="edit")
]
