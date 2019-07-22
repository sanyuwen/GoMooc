from django.db import models

from user.models import UserProfile
from course.models import Course


class UserAsk(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'userAsk'


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'courseComment'


class UserFavorite(models.Model):
    ENTITY = ((1, 'course'), (2, 'organization'), (3, 'teacher'))
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    favorite_id = models.IntegerField(default=1)
    favorite_type = models.IntegerField(choices=ENTITY, default=1)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'userFavorite'


class UserMessage(models.Model):
    user = models.IntegerField(default=0) # 0,for all people, 1, the user
    message = models.CharField(max_length=500)
    add_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = verbose_name = 'userMessage'


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'userCourse'
