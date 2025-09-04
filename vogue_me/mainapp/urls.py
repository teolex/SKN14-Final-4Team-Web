from django.urls import path

from . import views as v

app_name = 'mainapp'

urlpatterns = [
    path(''         , v.index       , name="index"),
    path('detail' , v.detail    , name="detail"),
]