from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from dopObrazovanieApp.models import Teacher, Favorites
import json


def homepage(request):
    if request.method == 'GET':
        args = {}
        args["teachers"] = Teacher.objects.all()
        args["favorites"] = Favorites.objects.all().count()
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
