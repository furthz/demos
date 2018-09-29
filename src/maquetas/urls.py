# -*- coding: utf-8 -*-
from django.conf.urls import url
from maquetas.views import ClaroView, TimView, VivoView, BradescoView, ItauView

# Create your views here.
urlpatterns = [
    url('claro/$', ClaroView.as_view(), name='ClaroIndex'),
    url('tim/$', TimView.as_view(), name='TimIndex'),
    url('vivo/$', VivoView.as_view(), name='VivoIndex'),
    url('bradesco/$', BradescoView.as_view(), name='BradescoIndex'),
    url('itau/$', ItauView.as_view(), name='ItauIndex'),

    # url(r'^grafico_barras/$', BarView.as_view(), name='bar'),
    # url(r'^demo/claro/$', DemoClaroView.as_view(), name='demo_claro'),
    # url(r'^demo/vivo/$', DemoVivoView.as_view(), name='demo_vivo'),
    # url(r'^demo/tim/$', DemoTimView.as_view(), name='demo_tim'),
    # url(r'^demo/itau/$', DemoItauView.as_view(), name='demo_itau'),

]