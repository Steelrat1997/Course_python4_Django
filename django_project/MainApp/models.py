from django.db import models

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()

   def __repr__(self):
      return f"Item: {self.name} Brand: {self.brand}  Count: {self.count}"

   def __str__(self):
      return f"Item:{self.name}        Brand:{self.brand}         Count:{self.count}"