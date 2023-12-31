# Generated by Django 4.2.4 on 2023-09-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_food_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='food',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
