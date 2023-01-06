from django.contrib import admin
# import your models here
from .models import Wolf, Feeding

# Register your models here
admin.site.register(Wolf)
# register the new Feeding Model 
admin.site.register(Feeding)

