# Generated by Django 2.1.7 on 2019-08-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsystem', '0002_auto_20190808_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]