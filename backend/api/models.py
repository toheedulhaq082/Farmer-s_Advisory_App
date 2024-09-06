from django.db import models
from django.utils import timezone

class Weather(models.Model):
    CITY_CHOICES = [
        ('Bahawalpur', 'Bahawalpur'),
        ('Multan', 'Multan'),
        ('Hyderabad', 'Hyderabad'),
    ]
    timestamp = models.DateTimeField(auto_now_add=True)
    # image_path = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    country = models.CharField(max_length=100)
    date = models.DateField()
    temp = models.FloatField()
    temp_feels_like = models.FloatField()
    precipitation = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    description = models.CharField(max_length=100)
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    wind_dir = models.CharField(max_length=100)
    timezone = models.IntegerField()
    day_0_temp = models.FloatField(default=0)
    day_1_temp = models.FloatField(default=0)
    day_2_temp = models.FloatField(default=0)
    day_3_temp = models.FloatField(default=0)
    day_4_temp = models.FloatField(default=0)
    day_5_temp = models.FloatField(default=0)
    day_6_temp = models.FloatField(default=0)
    day_7_temp = models.FloatField(default=0)
    day_1_name = models.CharField(max_length=10)  
    day_2_name = models.CharField(max_length=10)
    day_3_name = models.CharField(max_length=10)
    day_4_name = models.CharField(max_length=10)
    day_5_name = models.CharField(max_length=10)
    day_6_name = models.CharField(max_length=10)
    day_7_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.city
    
class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at =  models.DateTimeField(default=timezone.now, null=False)


    class Meta:
        db_table = 'province'

    def __str__(self):
        return self.name

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    name_urdu = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(default=0, max_digits=10, decimal_places=7)
    longitude = models.DecimalField(default=0, max_digits=10, decimal_places=7)
    altitude = models.IntegerField(default=0)
    radius = models.IntegerField(default=0)
    created_at =  models.DateTimeField(default=timezone.now, null=False)
    province=models.ForeignKey(Province, on_delete=models.PROTECT, null=True)


    class Meta:
        db_table = 'region'

    def __str__(self):
        return self.name

class Crop(models.Model):
    id = models.AutoField(primary_key=True)
    name_eng = models.CharField(max_length=255)
    name_urdu = models.CharField(max_length=255)
    created_at =  models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = 'crop'

    def __str__(self):
        return self.name_eng

class CropCoefficient(models.Model):
    id = models.AutoField(primary_key=True)
    crop = models.ForeignKey(Crop, on_delete=models.PROTECT)
    jan = models.FloatField(null=True, blank=True)
    feb = models.FloatField(null=True, blank=True)
    mar = models.FloatField(null=True, blank=True)
    apr = models.FloatField(null=True, blank=True)
    may = models.FloatField(null=True, blank=True)
    jun = models.FloatField(null=True, blank=True)
    jul = models.FloatField(null=True, blank=True)
    aug = models.FloatField(null=True, blank=True)
    sep = models.FloatField(null=True, blank=True)
    oct = models.FloatField(null=True, blank=True)
    nov = models.FloatField(null=True, blank=True)
    dec = models.FloatField(null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, null=True, blank=True)   
    created_at = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = 'crop_coefficient'

    def __str__(self):
        return self.crop.name_eng

class DistrictCrop(models.Model):
    id = models.AutoField(primary_key=True)
    crop = models.ForeignKey(Crop, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True)
    created_at =  models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = 'district_crop'

    def __str__(self):
        return self.crop.name_eng + ' - ' + self.region.name