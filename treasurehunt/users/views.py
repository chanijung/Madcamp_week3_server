from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from . import models as user_models
from .serializers import UserSerializer
import json
#serialize를 한다는 것은 json이나 xml 파일 등으로 바꾸어 주는 것.

@csrf_exempt
@api_view(["GET", "POST"])
def login(request):
    if request.method == "POST":
        print("login post")
        params_json = request.body.decode(encoding = "utf-8")
        data_json = json.loads(request.body)
        print(data_json)
        email = data_json["email"]
        login_method = data_json["method"]
        nickname = data_json["nickname"]
        uid = data_json["uid"]
        token = data_json["token"]
        try:
            user = user_models.User.objects.get(uid=uid)
            return Response("{Result:Exists}")
        except:
            if(login_method == "facebook.com"):
                user = user_models.User.objects.create(username=nickname, email=email, login_method=user_models.User.LOGIN_FACEBOOK, uid=uid, nickname=nickname, token=token)
                user.save()
                return Response("{Result:Post}")
            else:
                print("Method Error")
                return Response("{Result:Error}")
    elif request.method == "GET":
        print(request)
        return Response("GET")