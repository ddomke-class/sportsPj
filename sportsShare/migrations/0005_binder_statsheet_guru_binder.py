# Generated by Django 4.2 on 2024-04-09 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsShare', '0004_rename_typeguru_guru_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(verbose_name=True)),
                ('about', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Statsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('playerOneStats', models.CharField(max_length=200)),
                ('playerTwoStats', models.CharField(max_length=200)),
                ('binder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsShare.binder')),
            ],
        ),
        migrations.AddField(
            model_name='guru',
            name='binder',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsShare.binder'),
        ),
    ]
