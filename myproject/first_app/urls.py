from django.urls import path
from first_app import views

urlpatterns = [
    path("", views.homepage_view, name='homepage'),
    path("dashboard", views.dashboard_view, name='dashboard'),
    path("login", views.login_view, name='login'),
    path("signup", views.signup_view, name='signup'),
    path("logout", views.logout_view, name='logout'),
    path("profile", views.profile_view, name='profile'),
]
