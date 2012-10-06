from django.http import  HttpRequest, HttpResponse
import user_profile_service.views


# Create your views here.

def login(request):
    req = HttpRequest()
    resp = user_profile_service.views.detail(req, 0)
    return HttpResponse(resp, mimetype='application/json')

