from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import City, CourseOrganization, Teacher
from .forms import UserAskForm


class OrgView(View):
    def get(self, request):
        # get parameters
        city_id = request.GET.get('city', '')
        category = request.GET.get('ct', '')
        sort = request.GET.get('sort', '')

        # get filtered data
        all_citys = City.objects.all()
        all_orgs = CourseOrganization.objects.all()
        hot_orgs = all_orgs.order_by("-click_num")[:4]

        if city_id:
            all_orgs = all_orgs.filter(city_id = int(city_id))

        if category:
            all_orgs = all_orgs.filter(category=category)

        if sort == 'students':
            all_orgs = all_orgs.order_by('-student_num')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-course_num')

        org_nums = all_orgs.count()

        # pagination
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 3, request=request)
        all_orgs = p.page(page)

        return render(request, 'org-list.html', {'all_citys': all_citys,
                                                 'all_orgs': all_orgs,
                                                 'org_nums': org_nums,
                                                 'category': category,
                                                 'city_id': city_id,
                                                 'hot_orgs': hot_orgs})


class AddUserAskView(View):
    def post(self, request):
        ask_form = UserAskForm(request.POST)
        if ask_form.is_valid():
            ask_form.save(commit=True)
            return HttpResponse({'status': 'success'}, content_type='application/json')
        else:
            return HttpResponse({'status': 'fail', 'msg': 'Wrong data'}, content_type='application/json')


class OrgHomeView(View):
    def get(self, request):
        pass


class OrgCourseView(View):
    pass


class OrgDescView(View):
    pass


class AddFavView(View):
    pass


class TeacherListView(View):
    pass


class TeacherDetailView(View):
    pass


class OrgTeacherView(View):
    pass
