from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import render
import csv
import dateutil
import os
import pandas as pd


# Create your views here.
class DemoView(TemplateView):
    template_name = 'demos.html'

    def get(self, request, *args, **kwargs):
        df = pd.read_csv('C:/Users/raul_/PycharmProjects/demos/demos/src/static/csv/datos.csv', sep=',')

        df['Fecha'] = df['Fecha'].apply(dateutil.parser.parse, dayfirst=True)

        df['Fecha'] = df.Fecha.dt.strftime('%Y/%m')#.astype(dateutil.parser.parse)

        navegadores = df.groupby(['Navegador'])['Usuario']

        secciones = df.groupby(['Seccion','Fecha'])['Usuario'].count()

        #print(secciones)

        grupos = []
        for grupo, cant in navegadores:
            item = []
            # grupo1 = grupo[:len(grupo)-2]
            item.append(grupo)
            item.append(len(df.groupby(['Navegador'])['Usuario'].groups[grupo]))
            grupos.append(item)

        #print(grupos)

        myfile = open('C:/Users/raul_/PycharmProjects/demos/demos/src/static/csv/example3.csv', 'w')

        with myfile:
            writer = csv.writer(myfile)
            writer.writerows(grupos)

        print(df)

        data = pd.read_csv('C:/Users/raul_/PycharmProjects/demos/demos/src/static/csv/datos.csv', sep=',')
        return render(request, template_name=self.template_name, context={'datos': data})


class BarView(LoginRequiredMixin, TemplateView):
    template_name = 'bar.html'
