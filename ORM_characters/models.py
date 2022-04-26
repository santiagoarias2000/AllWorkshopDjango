from django.db import models


class Universe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_foundation = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'universos'


class Character(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=260)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characters'


class Powers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'powers'


class Powers_character(models.Model):
    powers = models.ForeignKey(Powers, on_delete=models.CASCADE)
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    number = models.IntegerField(100)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'powers_character'