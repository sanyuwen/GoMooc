__author__ = 'huang'
__date__ = '12/1/2018 11:11 PM'


from django.urls import path

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentsView

urlpatterns = [
    #课程列表页
    path('list/', CourseListView.as_view(), name="course_list"),

    #课程详情页
    path('detail/<int: course_id>/', CourseDetailView.as_view(), name="course_detail"),

    path('info/<int: course_id>/', CourseInfoView.as_view(), name="course_info"),

    #课程评论
    path('comment/<int: course_id>/', CommentsView.as_view(), name="course_comments"),

    #添加课程评论
    path('add_comment/', AddComentsView.as_view(), name="add_comment"),

]