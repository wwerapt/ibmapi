from django.db import models

# Create your models here.
class Demand(models.Model):
    day = models.IntegerField()  # Changed from CharField to IntegerField to match your new data structure

    def __str__(self):
        return str(self.day)

class Branch(models.Model):
    demand = models.ForeignKey(Demand, related_name='data', on_delete=models.CASCADE)
    branch_number = models.IntegerField()

    def __str__(self):
        return f"{self.demand.day} - Branch {self.branch_number}"

class Transaction(models.Model):
    branch = models.ForeignKey(Branch, related_name='transactions', on_delete=models.CASCADE)
    productA = models.IntegerField()
    productB = models.IntegerField()
    productC = models.IntegerField()
    productD = models.IntegerField()
    Gender = models.IntegerField()  # Assuming Gender is stored as an integer, modify this according to your actual data structure
    Age = models.IntegerField()

    def to_dict(self):
        return {
            "productA": self.productA,
            "productB": self.productB,
            "productC": self.productC,
            "productD": self.productD,
            "Gender": self.Gender,
            "Age": self.Age,
        }
