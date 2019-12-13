from django.contrib import admin
from .models import Sicilian_Pizza, Regular_Pizza, Pasta, Dinner_Platters, Salad, Toppings, Subs

# Register your models here.
admin.site.register(Dinner_Platters)
admin.site.register(Pasta)
admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Salad)
admin.site.register(Toppings)
admin.site.register(Subs)
