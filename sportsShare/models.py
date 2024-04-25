from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Binder(models.Model):
#List of choices for major value in database, human readable name
    title = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    is_active = models.BooleanField(True)
    about = models.CharField(max_length=200, blank=True)

#Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title

#Returns the URL to access a particular instance of MyModelName.
#if you define this method then Django will automatically
# add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('binder-detail', args=[str(self.id)])

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
    binder = models.OneToOneField(Binder, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('guru-detail', args=[str(self.id)])

class Statsheet(models.Model):
#List of choices for major value in database, human readable name
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    playerOneName = models.CharField(max_length=200)
    playerOneYards = models.PositiveSmallIntegerField(default=0)
    playerOneTouchdowns = models.PositiveSmallIntegerField(default=0)
    playerTwoName = models.CharField(max_length=200)
    playerTwoYards = models.PositiveSmallIntegerField(default=0)
    playerTwoTouchdowns = models.PositiveSmallIntegerField(default=0)
    binder = models.ForeignKey(Binder, on_delete=models.CASCADE, null=True)

#Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title

#Returns the URL to access a particular instance of MyModelName.
#if you define this method then Django will automatically
# add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('statsheet-detail', args=[str(self.id)])