#from django.urls import path
from django.conf.urls import include, url

from . import views

app_name = 'accounts'
urlpatterns = [
    url('login/', views.LoginView.as_view(), name="login"),
    url('logout/', views.LogoutView.as_view(), name='logout'),
    url('signup/', views.SignUpView.as_view(), name='signup'),
    url('password-change/', views.PasswordChangeView.as_view(),
         name='password-change'),
    url('password-reset/', views.PasswordResetView.as_view(),
         name='password-reset'),
    url('password-reset-done/', views.PasswordResetDoneView.as_view(),
         name='password-reset-done'),
    url('password-reset/<uuid:uidb64>/<slug:token>/',
         views.PasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
]
