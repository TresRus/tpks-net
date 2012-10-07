# Create your views here.
from django.http import HttpResponse
import json
from user_profile_service.models import User


def detail(request, user_id):
    response_data = {}
    profiles = User.objects.filter(id=user_id)
    if profiles.count() == 0:
        response_data['status'] = 'Fail'
        response_data['detail'] = 'No such user in service'
        return HttpResponse(json.dumps(response_data), mimetype='application/json')
    else:	
    	profile = profiles[0]
        response_data['status'] = 'OK'
        response_data['nqme'] = profile.nqme
        response_data['surname'] = profile.surname
        response_data['patronymic']  = profile.patronymic
        response_data['post'] = profile.post
        response_data['home_phonenumber'] = profile.home_phonenumber
        response_data['mobile_phonenumber'] = profile.mobile_phonenumber
        response_data['workspace_address'] = profile.workspace_address
        return HttpResponse(json.dumps(response_data), mimetype='application/json')

def create(request, user_id):
    response_data = {}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User(login = username, password = password,nqme = 'Default', surname = 'Default',
            patronymic = 'Default', post = 'Default',home_phonenumber = 'Default',
            mobile_phonenumber = 'Default',workspace_address = 'Default')
        user.id = user_id
        user.save()

        response_data['status'] = 'OK'
        response_data['nqme'] = user.nqme
        response_data['surname'] = user.surname
        response_data['patronymic']  = user.patronymic
        response_data['post'] = user.post
        response_data['home_phonenumber'] = user.home_phonenumber
        response_data['mobile_phonenumber'] = user.mobile_phonenumber
        response_data['workspace_address'] = user.workspace_address
        return HttpResponse(json.dumps(response_data), mimetype='application/json')

    response_data['status'] = 'Fail'
    return HttpResponse(json.dumps(response_data), mimetype='application/json')
