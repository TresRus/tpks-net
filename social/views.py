
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import  HttpRequest, HttpResponse
import user_profile_service.views
import json
import logging


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #check if there is such a user in UserProfileService
                req = HttpRequest()
                response = user_profile_service.views.detail(req, user.id)
                resp = json.loads(response.content)
                #if all there is -> give user page with info
                #if there is no such user -> create him ( this logic is just for test)
                if resp["status"] == "OK":
                    return HttpResponse(response, mimetype="application/json")
                elif resp["status"] == "Fail":
                    if resp["detail"] == "No such user in service":
                        req = HttpRequest()
                        req.POST.__setitem__('username', username)
                        req.POST.__setitem__('password', password)
                        response = user_profile_service.views.create(req, user.id)
                        resp = json.loads(response.content)
                        #check if all is right
                        if resp["status"] == "OK":
                            return HttpResponse(response, mimetype="application/json")
                        else:
                            #if things still look bad, then dovai, do svidania !
                            logout(request, user)
                            state = state = "Sorry, but you are looser"
                            return render_to_response('auth.html', {'state':state, 'username': username}, context_instance=RequestContext(request))
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect." 
    
    return render_to_response('auth.html', {'state':state, 'username': username}, context_instance=RequestContext(request))