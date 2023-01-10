from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
# new code above
# Add the WOLF class & list and view function below the imports
class Wolf(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)

  def __str__(self):
    return self.name
    

  def get_absolute_url(self):
    return reverse('detail', kwargs={'wolf_id': self.id})

  def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
   # Create a wolf_id FK
  wolf = models.ForeignKey(Wolf, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

 # change the default sort
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    wolf = models.ForeignKey(Wolf, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for wolf_id: {self.wolf_id} @{self.url}"