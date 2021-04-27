from django.db import models

# Create your models here.

class Chart(models.Model):

    humidity = models.FloatField(default = 10)
    light_intensity = models.FloatField(default = 0)
    air_temp = models.FloatField(default = 0)
    soil_temp = models.FloatField(default = 0)
    time = models.CharField(max_length = 30,default = 0)



    def __str__(self):
        return("Humidity: {}\n"
        "Air_temperature: {}\n"
        "Soil_temperature: {}\n"
        "Light_intensity: {}\n"
        "Time: {}".format(self.humidity, self.air_temp, self.soil_temp, self.light_intensity, self.time))

