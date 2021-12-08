from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=68)
    ratting = models.IntegerField(
    default=1,
    validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])     #Sets the range of ratting between [1,10]
    verdict = models.CharField(max_length=100)
