__author__ = 'huang'
__date__ = '12/1/2018 9:55 PM'

import xadmin

from .models import City, Teacher, CourseOrganization


class CityAdmin(object):
    list_display = ['name', 'description', 'add_time']
    search_fields = ['name', 'description']
    list_filter = ['name', 'description', 'add_time']


class TeacherAdmin(object):
    list_display = ['organization', 'name', 'company', 'work_years']
    search_fields = ['organization', 'name', 'company', 'work_years']
    list_filter = ['organization', 'name', 'company', 'work_years']


class CourseOrganizationAdmin(object):
    list_display = ['name', 'description', 'category', 'city', 'click_num', 'favorite_num']
    search_fields = ['name', 'description', 'category', 'city', 'click_num', 'favorite_num']
    list_filter = ['name', 'description', 'category', 'city', 'click_num', 'favorite_num']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrganization, CourseOrganizationAdmin)
