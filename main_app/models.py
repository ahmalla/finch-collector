from django.db import models
from django.urls import reverse



MEALS = (
    ("M", "Morning"),
    ("N", "Nothing"),
    ("D", "Dinner")
)


class Trinket(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trinkets_detail', kwargs={'pk': self.id})




# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    trinkets = models.ManyToManyField(Trinket)

    def __str__(self):
        return f'{self.name}' ({self.id})

    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})


class Feeding(models.Model):
    date = models.DateField("feeding date")
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS [0] [0])
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    