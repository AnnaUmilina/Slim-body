# Generated by Django 4.2.4 on 2023-08-18 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_articles_description_alter_articles_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewiewrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.recipies'),
        ),
    ]
