from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Member)
admin.site.register(Cart)
admin.site.register(Checkout)
admin.site.register(Order)

