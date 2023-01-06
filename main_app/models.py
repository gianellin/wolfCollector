from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
# Add the Cat class & list and view function below the imports
class Wolf(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
    
  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'wolf_id': self.id})
