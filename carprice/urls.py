
from django.contrib import admin
from django.urls import path
from carprice import views
urlpatterns = [
   path("",views.index,name="carprice"),
   path("predict",views.predict,name="predict")
]