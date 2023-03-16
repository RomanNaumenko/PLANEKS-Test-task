from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.scheme_list)),
    path('create/', login_required(views.scheme_create)),
    path('list/', login_required(views.scheme_list))
]