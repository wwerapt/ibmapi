# myapi/serializers.py
from rest_framework import serializers
from .models import Demand, DemandBranch

class DemandBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandBranch
        fields = ('branch_number', 'demand_product_A_value', 'demand_product_B_value', 'demand_product_C_value', 'demand_product_D_value')

class DemandSerializer(serializers.ModelSerializer):
    branches = DemandBranchSerializer(source='demandbranch_set', many=True, read_only=True)

    class Meta:
        model = Demand
        fields = ('day', 'branches')