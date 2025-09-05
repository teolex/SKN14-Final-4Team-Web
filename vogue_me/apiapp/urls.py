from django.urls import path

from . import views as v

app_name = 'apiapp'

urlpatterns = [
    path('ask', v.ask_api , name="ask_api"),
]