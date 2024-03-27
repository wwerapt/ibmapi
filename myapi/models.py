from django.db import models

# Create your models here.
class Demand(models.Model):
    day = models.CharField(max_length=100)

    def __str__(self):
        return self.day

class DemandBranch(models.Model):
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    branch_number = models.IntegerField()
    demand_value = models.IntegerField()

    def __str__(self):
        return f"{self.demand.day} - Branch {self.branch_number}"

    def to_dict(self):
        return {
            "branch": self.branch_number,
            "demand": self.demand_value
        }