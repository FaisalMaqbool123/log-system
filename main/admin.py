from django.contrib import admin
from . models import Product,Log
# Register your models here.
@admin.register(Product)
class productadmin(admin.ModelAdmin):
    fields=['id','title','price','description']
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    fields=['id','log_type' ,'message','created_at']