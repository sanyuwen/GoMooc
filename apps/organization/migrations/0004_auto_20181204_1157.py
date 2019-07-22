# Generated by Django 2.0 on 2018-12-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_courseorganization_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorganization',
            name='category',
            field=models.CharField(choices=[('training', 'training camps'), ('person', 'person'), ('university', 'university')], default='university', max_length=20),
        ),
    ]
