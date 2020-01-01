from django.urls import path,re_path
from . import views
App_Name='PetrolPumpApp'

urlpatterns = [
    re_path(r'^$',views.PetrolData,name="petrol"),
    re_path(r'^diesel/$',views.DieselData,name="diesel"),


]