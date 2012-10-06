# Create your views here.
from django.http import HttpResponse
import json

def detail(request, user_id):
    response_data = {user_id: "That's his data"}
    return HttpResponse(json.dumps(response_data), mimetype='application/json')
