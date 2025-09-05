from django.urls import path

from . import views as v

app_name = 'mainapp'

urlpatterns = [
    path(''                 , v.index , name="index"),
    path('detail/<int:id>'  , v.detail, name="detail"),
]