from django.shortcuts import render
from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.

class CountryList(APIView):
    def get(self, request):
        countries = Country.objects.all()  # Retrieve all countries
        serializer = CountrySerializer(countries, many=True)  # Serialize the countries
        return Response(serializer.data)

    def post(self, request):
        serializer = CountrySerializer(data=request.data)  # Deserialize the incoming data
        if serializer.is_valid():
            serializer.save()  # Save the new country
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryDetail(APIView):
    def get_object(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return None

    def get(self, request, pk):
        country = self.get_object(pk)
        if country is not None:
            serializer = CountrySerializer(country)
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        country = self.get_object(pk)
        if country is not None:
            serializer = CountrySerializer(country, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        country = self.get_object(pk)
        if country is not None:
            country.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    

