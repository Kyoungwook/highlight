# Generated by Django 3.1.1 on 2020-10-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20201004_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='averageGrade',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.FloatField(default=0),
        ),
    ]