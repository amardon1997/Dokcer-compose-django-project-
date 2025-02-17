from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from blog.models import Country

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})