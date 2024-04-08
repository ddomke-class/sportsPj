from django.db import models

# Create your models here.
class Guru(models.Model):

#List of choices for major value in database, human readable name
    TYPEGURU = (
        ('Bar Owner', 'Matchup Stats'),
        ('Analyst', 'Team Comparison'),
        ('Gambler', 'Single Player Stats'),
    )
    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    major = models.CharField(max_length=200, choices=TYPEGURU, blank = True)
