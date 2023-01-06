from django.db import models

# Create your models here.
# Add the Cat class & list and view function below the imports
class Wolf(models.Model):
    name =models.CharField(max_length=100)
    breed =models.CharField(max_length=100)
    description =models.TextField(max_length=250)
    age = models.IntegerField()


