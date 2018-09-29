from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ClaroView(LoginRequiredMixin, TemplateView):
    template_name = 'claro/demo_claro.html'


class TimView(LoginRequiredMixin, TemplateView):
    template_name = 'tim/demo_tim.html'


class VivoView(LoginRequiredMixin, TemplateView):
    template_name = 'vivo/demo_vivo.html'


class BradescoView(LoginRequiredMixin, TemplateView):
    template_name = 'bradesco/demo_bradesco.html'


class ItauView(LoginRequiredMixin, TemplateView):
    template_name = 'itau/demo_itau.html'


