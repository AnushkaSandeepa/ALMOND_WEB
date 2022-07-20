from django.db import models

# Create your models here.

class Session(models.Model):
	session_id = models.TextField(max_length=14)
	model_id = models.TextField(max_length=30)
	date = models.TextField(max_length=8)
	time = models.TextField(max_length=6)
	invest_id = models.TextField(max_length=50, null=False)
	investigator = models.TextField(max_length=50, null=False)
	country = models.TextField(max_length=15)
 
class MeasureTemp(models.Model):
    click_id = models.TextField(max_length=14)
    X1 = models.FloatField(null=True)
    Y1 = models.FloatField(null=True)
    X2 = models.FloatField(null=True)
    Y2 = models.FloatField(null=True)
      
class Measurements(models.Model):
    measure_id = models.TextField(max_length=14)
    session_id = models.TextField(max_length=14)
    X1 = models.FloatField(null=True)
    Y1 = models.FloatField(null=True)
    X2 = models.FloatField(null=True)
    Y2 = models.FloatField(null=True)
    place = models.TextField(max_length=30)
    distance = models.TextField(max_length=30)
  
class ModelInfo(models.Model):
    model_id = models.TextField(max_length=14)
    cloth_type = models.TextField(max_length=30)
    sh_width = models.TextField(max_length=30)
    chest = models.TextField(max_length=30)
    length = models.TextField(max_length=30)
    width = models.TextField(max_length=30)
    sl_length = models.TextField(max_length=30)
    nk_width = models.TextField(max_length=30)
    c_rgb = models.TextField(max_length=30)
    c_html = models.TextField(max_length=30)		