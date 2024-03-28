# myapi/serializers.py
from rest_framework import serializers
from .models import Demand, Branch, Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('productA', 'productB', 'productC', 'productD', 'Gender', 'Age')

class BranchSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = ('branch_number', 'transactions')

class DemandSerializer(serializers.ModelSerializer):
    data = BranchSerializer(many=True, read_only=True)  # Removed source='data'

    class Meta:
        model = Demand
        fields = ('day', 'data')
