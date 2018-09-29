from django.conf.urls import url
from . import views


# Create your views here.
urlpatterns = [
        url('demo/', views.DemoView.as_view(), name='demos'),
    ]