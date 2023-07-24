from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.place.name} the restaurant"


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    """
        with a foreign key relationship, multiple instances of the model 
        that owns the foreign key can refer to the same instance of the related model.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} the waiter at {self.restaurant}"
