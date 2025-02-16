from django.contrib import admin
from .models import Product, SurveyResponse

# Register your models here.

admin.site.register(Product)
admin.site.register(SurveyResponse)