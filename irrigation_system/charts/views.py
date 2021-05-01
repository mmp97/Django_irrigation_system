from django.shortcuts import render
from django.views.generic import  TemplateView
from django.http import JsonResponse, HttpResponse
from .models import Chart
import json
import datetime

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    #data_form = DataSelectForm

    def post(self, request , **kwargs):
        context = super().get_context_data(**kwargs)
        hours = [(datetime.time(hour = int(i/4)).strftime('    %I   %p   ')) for i in range(96)]

        humidity= Chart.objects.filter(name = "humidity").last()
        light_intensity = Chart.objects.filter(name = "light_intensity").last()
        air_temp = Chart.objects.filter(name = "air_temp").last()
        soil_temp = Chart.objects.filter(name = "soil_temp").last()
        time = hours         
        context["qs"] = {"humidity":humidity,
                   "light_intensity": light_intensity, 
                   "air_temp": air_temp, 
                   "soil_temp": soil_temp,
                   "time": time}
        return render(request, self.template_name, context )

class ChartsView(TemplateView):
    template_name = 'charts.html'
    #data_form = DataSelectForm

    def post(self, request , **kwargs):
        context = super().get_context_data(**kwargs)
        hours = [(datetime.time(hour = int(i/4)).strftime('    %I   %p   ')) for i in range(96)]

        humidity= list(Chart.objects.values_list("humidity", flat=True))
        light_intensity = list(Chart.objects.values_list("light_intensity", flat=True))
        air_temp = list(Chart.objects.values_list("air_temp", flat=True))
        soil_temp = list(Chart.objects.values_list("soil_temp", flat=True))
        time = hours #list(Chart.objects.values_list("time", flat=True).order_by('id').annotate(idmod4=F('id') % period).filter(idmod4=0))
        
        context["qs"] = {"humidity":humidity,
                   "light_intensity": light_intensity, 
                   "air_temp": air_temp, 
                   "soil_temp": soil_temp,
                   "time": time}
        return render(request, self.template_name, context )
