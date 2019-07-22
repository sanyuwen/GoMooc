from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)
    add_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = verbose_name = 'city'

    def __str__(self):
        return self.name


class CourseOrganization(models.Model):
    CATEGORY = (("training", "training camps"), ("person", "person"), ("university", "university"))
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    click_num = models.IntegerField(default=0)
    favorite_num = models.IntegerField(default=0)
    student_num = models.IntegerField(default=0)
    course_num = models.IntegerField(default=0)
    category = models.CharField(default="university", max_length=20, choices=CATEGORY)
    image = models.ImageField(upload_to='organization/%Y/%M', default='organization/default.png', max_length=100)
    address = models.CharField(max_length=150)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'courseOrganization'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    organization = models.ForeignKey(CourseOrganization, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    work_years = models.IntegerField(default=0)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    points = models.CharField(max_length=50)
    click_num = models.IntegerField(default=0)
    favorite_num = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'teacher'

    def __str__(self):
        return self.name

