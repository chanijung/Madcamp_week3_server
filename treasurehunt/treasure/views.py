from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from users import models as user_models
from . import models as treasures
#serialize를 한다는 것은 json이나 xml 파일 등으로 바꾸어 주는 것.

@csrf_exempt
@api_view(["GET", "POST"])
def hide(request):
    if request.method == "POST":
        print("hide post")
        params_json = request.body.decode(encoding = "utf-8")
        print(request.body)
        print(params_json)
        data_json = json.loads(request.body)
        # data_json = json.loads(params_json)
        print(data_json)
        hid = data_json["hid"]
        print("hid: ",hid)
        hider = user_models.User.objects.get(uid=hid)
        latitude = data_json["latitude"]
        longitude = data_json["longitude"]

        treasure = treasures.Treasure.objects.create(hider=hider, latitude=latitude, longitude=longitude)
        treasure.save()


        return Response("{Result:Post}")

        # email = data_json["email"]
        # login_method = data_json["method"]
        # nickname = data_json["nickname"]
        # uid = data_json["uid"]
        # try:
        #     user = user_models.User.objects.get(uid=uid)
        #     return Response("{Result:Exists}")
        # except:
        #     if(login_method == "facebook.com"):
        #         user = user_models.User.objects.create(username=nickname, email=email, login_method=user_models.User.LOGIN_FACEBOOK, uid=uid, nickname=nickname)
        #         user.save()
        #         return Response("{Result:Post}")
        #     else:
        #         print("Method Error")
        #         return Response("{Result:Error}")
    # elif request.method == "GET":
    #     print(request)
    #     return Response("GET")