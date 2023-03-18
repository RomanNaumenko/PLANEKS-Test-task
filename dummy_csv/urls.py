from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', login_required(views.scheme_listing)),
    path('create/', login_required(views.scheme_creation)),
    path('list/', login_required(views.scheme_listing)),
    path('edit/<int:id>/', login_required(views.scheme_editing.as_view())),
    path('delete/<int:id>/', login_required(views.scheme_deleting.as_view())),
    path('download/<int:id>/', login_required(views.media_download)),
    path('generate/<int:id>/', login_required(views.csv_generator_setting)),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'))
]

