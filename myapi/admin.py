from django.contrib import admin
from .models import Demand, Branch, Transaction  # Updated imports to include Branch and Transaction

# Register your models here.
admin.site.register(Demand)
admin.site.register(Branch)
admin.site.register(Transaction)
