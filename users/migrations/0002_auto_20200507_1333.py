# Generated by Django 3.0.6 on 2020-05-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_pics'),
        ),
    ]
