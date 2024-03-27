from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DemandSerializer
from .models import Demand, DemandBranch

class DemandViewSet(viewsets.ModelViewSet):
    serializer_class = DemandSerializer

    def get_queryset(self):
        return Demand.objects.all().order_by('day')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        formatted_data = []
        for demand_instance in queryset:
            formatted_data.append(demand_to_dict(demand_instance))
        return Response(formatted_data)

def demand_to_dict(demand):
    data = {
        "day": demand.day,
        "data": []
    }
    branches = DemandBranch.objects.filter(demand=demand)
    for branch in branches:
        data["data"].append(branch.to_dict())
    return data
