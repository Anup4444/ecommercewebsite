# Generated by Django 3.2.9 on 2022-05-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220520_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Ecoms/pimg'),
        ),
    ]