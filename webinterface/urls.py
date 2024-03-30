from django.urls import path
from .views import DemandGenerationView, generate_demand, success_view  # Make sure to import success_view

urlpatterns = [
    path('', DemandGenerationView.as_view(), name='base_demand_generation'),
    path('demand/generate/', generate_demand, name='generate_demand'),
    path('success/', success_view, name='success'),  # Now using the imported success_view
]
