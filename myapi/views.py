# myapi/views.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DemandSerializer
from .models import Demand, Branch  # Import Branch instead of DemandBranch

class DemandViewSet(viewsets.ModelViewSet):
    serializer_class = DemandSerializer

    def get_queryset(self):
        return Demand.objects.all().order_by('day')

# If you're still looking to convert Demand instances to dictionaries manually (for custom response structures or other reasons), update this function:
def demand_to_dict(demand):
    # Updated to reflect new model relationships and structure
    data = {
        "day": demand.day,
        "data": []
    }
    branches = Branch.objects.filter(demand=demand)  # Using Branch model
    for branch in branches:
        branch_data = {
            "branch": branch.branch_number,
            "transactions": [transaction.to_dict() for transaction in branch.transactions.all()]
        }
        data["data"].append(branch_data)
    return data

