# Generated by Django 3.2.9 on 2021-12-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]