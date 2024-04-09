# Generated by Django 4.2 on 2024-04-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsShare', '0005_binder_statsheet_guru_binder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statsheet',
            old_name='playerOneStats',
            new_name='playerOneName',
        ),
        migrations.RenameField(
            model_name='statsheet',
            old_name='playerTwoStats',
            new_name='playerTwoName',
        ),
        migrations.AddField(
            model_name='statsheet',
            name='playerOneTouchdowns',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsheet',
            name='playerOneYards',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsheet',
            name='playerTwoTouchdowns',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statsheet',
            name='playerTwoYards',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]