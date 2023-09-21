from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Product),
admin.site.register(Order),
admin.site.register(OrderItem),
admin.site.register(Cart),
admin.site.register(Review),
admin.site.register(Payment),
admin.site.register(CustomUser, UserAdmin)