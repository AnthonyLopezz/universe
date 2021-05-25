from django.db import models


# Create your models here.

# Model universe.

class Universe (models.Model):
    name = models.CharField(max_length=30)
    date_foundation = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'universe'


# Model characters.

class Character(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characters'


# Model powers.

class Powers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'powers'


# models ManyToMany powers and characters.

class power_character(models.Model):
    power = models.ForeignKey(Powers, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    scale = models.CharField(max_length=100)

    def __str__(self):
        return self.scale

    class Meta:
        db_table = 'powers_characters'
