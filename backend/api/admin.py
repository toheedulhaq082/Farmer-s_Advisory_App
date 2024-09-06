from django.contrib import admin
from api.models import Weather
from api.models import Province
from api.models import Region
from api.models import Crop
from api.models import CropCoefficient
from api.models import DistrictCrop

# Register your models here.
admin.site.register(Weather)
admin.site.register(Province)
admin.site.register(Region)
admin.site.register(Crop)
admin.site.register(CropCoefficient)
admin.site.register(DistrictCrop)
