__author__ = 'huang'
__date__ = '12/1/2018 9:22 PM'


import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'description', 'detail', 'level', 'learn_time', 'student_num']
    search_fields = ['name', 'description', 'detail', 'level', 'student_num']
    list_filter = ['name', 'description', 'detail', 'level', 'learn_time', 'student_num']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['Lesson', 'name', 'add_time']
    search_fields = ['Lesson', 'name']
    list_filter = ['Lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['Course', 'name', 'download', 'add_time']
    search_fields = ['Course', 'name', 'download']
    list_filter = ['Course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

