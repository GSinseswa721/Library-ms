# Generated by Django 4.0.6 on 2022-08-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library_user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
