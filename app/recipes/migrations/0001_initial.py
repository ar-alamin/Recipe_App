# Generated by Django 5.1.1 on 2024-09-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_des', models.TextField()),
                ('recipe_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
