# Generated by Django 2.0 on 2018-12-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20181204_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorganization',
            name='course_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courseorganization',
            name='student_num',
            field=models.IntegerField(default=0),
        ),
    ]