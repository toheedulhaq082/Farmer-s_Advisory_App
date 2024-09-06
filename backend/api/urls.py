from django.urls import path
from .views import WeatherList, CropCoefficientByCropRegionView

urlpatterns = [
    path('<str:city_name>/', WeatherList.as_view(), name='weatherlist'),
    path('crop-coefficients/<str:crop_name>/<str:region_name>/<int:number>/', CropCoefficientByCropRegionView.as_view(), name='crop_coefficients'),
]