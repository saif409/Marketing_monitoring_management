from django.contrib import admin
from django.contrib import admin
from.models import Country,Division,District,SubDistrict,Surveyor,CollectData,AssignDataCollector,ServiceCategory,Package

# Register your models here.

admin.site.register(Country)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Surveyor)
admin.site.register(CollectData)
admin.site.register(AssignDataCollector)
admin.site.register(ServiceCategory)
admin.site.register(Package)
