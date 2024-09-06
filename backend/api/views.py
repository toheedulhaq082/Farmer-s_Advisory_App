from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Weather, CropCoefficient, Crop, Region, DistrictCrop
from .serializers import WeatherSerializer, CropCoefficientSerializer
from .helper import getPrediction, filter_current_month, get_day_temp
from rest_framework.response import Response
from rest_framework import status

class WeatherList(ListAPIView):
    serializer_class = WeatherSerializer

    def get_queryset(self):
        city_name = self.kwargs['city_name']
        pred = getPrediction(city_name)
        return Weather.objects.filter(city=city_name).order_by('-timestamp')[:1]
    

class CropCoefficientByCropRegionView(APIView):

    def get(self, request, crop_name, region_name, number, format=None):
        
        try:
            print(crop_name, region_name, number)
            getPrediction(region_name)
            # Find the Crop object by name
            crop = Crop.objects.get(name_eng=crop_name)
            
            # Find the Region object by name
            region = Region.objects.get(name=region_name)
            
            # Find the Weather object by city name
            weather = Weather.objects.filter(city=region_name).order_by('-timestamp')[:1].first()
            
            # Find DistrictCrop entries linking Crop and Region
            district_crops = DistrictCrop.objects.filter(crop=crop, region=region)
            
            if not district_crops.exists():
                return Response({'error': f'No district crops found for crop: {crop_name} in region: {region_name}'}, status=status.HTTP_404_NOT_FOUND)
            
            # Get provinces related to the district crops
            provinces = [dc.region.province for dc in district_crops if dc.region.province]

                # Filter CropCoefficient by crop and related provinces
            crop_coefficients = CropCoefficient.objects.filter(crop=crop)
            
            serializer = CropCoefficientSerializer(crop_coefficients, many=True)
            serializer_data = filter_current_month(serializer.data)

            weather_data = None
            if weather:
                weather_serializer = WeatherSerializer(weather)
                weather_data = weather_serializer.data
                weather_data = get_day_temp(weather_data, number)
            # Combine crop coefficient and weather data in the response
            response_data = {
                'crop_coefficients': serializer_data,
                'weather': weather_data,
            }
    
            return Response(response_data, status=status.HTTP_200_OK)


        except Crop.DoesNotExist:
            return Response({'error': f'Crop not found: {crop_name}'}, status=status.HTTP_404_NOT_FOUND)
        except Region.DoesNotExist:
            return Response({'error': f'Region not found: {region_name}'}, status=status.HTTP_404_NOT_FOUND)

