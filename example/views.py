# example/views.py
from datetime import datetime
from django.http import JsonResponse

def apple_app_site_association(request):
    response_data = {
        "applinks": {
            "apps": [],
            "details": [
                {
                    "appID": "TEAM_ID.com.example.moneyPlanFlutter",
                    "paths": [ "/auth" ]
                }
            ]
        }
    }
    return JsonResponse(response_data)