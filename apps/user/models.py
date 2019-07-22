from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    GENDER = (('M', 'male'),('F', 'female'))
    nickname = models.CharField(max_length=50, default='')
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='F')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='user_images/%Y/%M', default='user_images/default.png', max_length=100)

    class Meta:
        verbose_name_plural = verbose_name = 'user'

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    EMAILSENT = (("register", "register"), ("forget", "reset_password"), ("update_email", "update_email"))
    code = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    send_type = models.CharField(max_length=1, choices=EMAILSENT)
    send_type = models.CharField(choices=EMAILSENT,
                                 max_length=30)
    send_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'verificationCode'

    def __str__(self):
        return '{}({})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/%Y/%M', default='banners/default.png', max_length=100)
    url = models.URLField(max_length=200)
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'banner'





