# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from dopObrazovanieApp.models import Teacher, Favorites
import json


def homepage(request):
    if request.method == 'GET':
        args = {}
        sort = request.GET.get("SortField", None)
        sort_direction = request.GET.get("SortDirection", "-")
        filter_metro = request.GET.get("FilterMetroField", None)
        filter_place = request.GET.get("FilterPlace", None)
        filter_subject = request.GET.get("FilterSubjField", None)

        if filter_metro == u"Все":
            filter_metro = None
        if filter_subject == u"Все":
            filter_subject = None

        teachers = Teacher.objects.all()

        if filter_metro:
            teachers = teachers.filter(Metro__contains=filter_metro)
        if filter_place:
            teachers = teachers.filter(ComeHome__contains=filter_place)
        if filter_subject:
            teachers = teachers.filter(Subjects__contains=filter_subject)

        if sort:
            sort = sort_direction + sort
            teachers = teachers.order_by(sort)
        args["teachers"] = teachers
        args["favorites"] = Favorites.objects.all().count()
        args["teachersNumber"] = Teacher.objects.all().count()
        return render_to_response('home.html', args, RequestContext(request))
    elif request.method == 'POST':
        teacher_id = int(request.POST.get("TeacherID", -1))
        if teacher_id == -1:
            response = {'status': -1}
        else:
            if request.POST["operationType"] == "add":
                favorite = Favorites()
                favorite.FavoriteTeacher = Teacher.objects.filter(pk=teacher_id)[0]
                favorite.save()
            elif request.POST["operationType"] == "delete":
                favorite = Favorites.objects.filter(FavoriteTeacher__id=teacher_id)[0]
                favorite.delete()
            response = {'status': 0}
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return HttpResponse(status=404)


def contactpage(request):
    return render_to_response('contact.html')


def aboutpage(request):
    return render_to_response('about.html')


def favoritespage(request):
    args = {}
    args["favorites"] = Favorites.objects.all()
    return render_to_response('favorites.html', args, RequestContext(request))
