from django.db import models

# Create your models here.
class Demand(models.Model):
    day = models.CharField(max_length=100)

    def __str__(self):
        return self.day

class DemandBranch(models.Model):
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    branch_number = models.IntegerField()
    demand_product_A_value = models.IntegerField(null=True)
    demand_product_B_value = models.IntegerField(null=True)
    demand_product_C_value = models.IntegerField(null=True)
    demand_product_D_value = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.demand.day} - Branch {self.branch_number}"

    def to_dict(self):
        return {
            "branch": self.branch_number,
            "demand_product_A": self.demand_product_A_value,
            "demand_product_B": self.demand_product_B_value,
            "demand_product_C": self.demand_product_C_value,
            "demand_product_D": self.demand_product_D_value
        }