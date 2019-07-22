# Generated by Django 2.1.3 on 2018-12-01 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('detail', models.TextField()),
                ('level', models.CharField(choices=[('*', 'easy'), ('**', 'medium'), ('***', 'hard')], max_length=3)),
                ('learn_time', models.IntegerField(default=0)),
                ('student_num', models.IntegerField(default=0)),
                ('favorite_num', models.IntegerField(default=0)),
                ('image', models.ImageField(default='courses/default.png', upload_to='courses/%Y/%M')),
                ('click_num', models.IntegerField(default=0)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('download', models.FileField(upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
            options={
                'verbose_name': 'courseResource',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Lesson')),
            ],
        ),
    ]