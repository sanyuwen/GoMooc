from django.db import models

from organization.models import CourseOrganization


class Course(models.Model):
    LEVEL = (('*', 'easy'), ('**', 'medium'), ('***', 'hard'))
    course_org = models.ForeignKey(CourseOrganization, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    detail = models.TextField()
    level = models.CharField(max_length=3, choices=LEVEL)
    learn_time = models.IntegerField(default=0)
    student_num = models.IntegerField(default=0)
    favorite_num = models.IntegerField(default=0)
    image = models.ImageField(upload_to='courses/%Y/%M', default='courses/default.png', max_length=100)
    click_num = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'course'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'lesson'


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'video'


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    download = models.FileField()

    class Meta:
        verbose_name_plural = verbose_name = 'courseResource'





