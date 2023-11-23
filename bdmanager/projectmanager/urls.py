from django.urls import path
from .views import permit_create, project_form, sale_form,get_partner_share

urlpatterns = [
    path("permit_create/", permit_create, name="permit_create"),
    path("project_create/", project_form, name="project_create"),
    path("sale_create/", sale_form, name="sale_create"),
    path("get_partner_share/", get_partner_share, name="get_partner_share")
]
