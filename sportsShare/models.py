from django.db import models
from django.urls import reverse

# Create your models here.
class Guru(models.Model):

#List of choices for major value in database, human readable name
    TYPEGURU = (
        ('Bar Owner', 'Matchup Stats'),
        ('Analyst', 'Team Comparison'),
        ('Gambler', 'Single Player Stats'),
        ('Newbie', 'Exploring a New World'),
    )
    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    experience = models.PositiveSmallIntegerField(default=0)
    Type = models.CharField(max_length=200, choices=TYPEGURU, default='Newbie')

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('guru-detail', args=[str(self.id)])
