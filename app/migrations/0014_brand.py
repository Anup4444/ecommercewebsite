# Generated by Django 3.2.9 on 2022-05-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_order_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]