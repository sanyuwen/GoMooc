# Generated by Django 2.0 on 2018-12-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20181201_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorganization',
            name='category',
            field=models.CharField(choices=[('training', 'training camps'), ('person', 'person'), ('university', 'university')], default='training', max_length=20),
        ),
    ]
