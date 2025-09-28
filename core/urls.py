from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import home, signup, login, dashboard, healthz, metrics

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/',  auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path("healthz/", healthz, name="healthz"),
    path('metrics/', metrics, name='metrics'),
]