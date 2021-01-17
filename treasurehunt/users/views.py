from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from . import models as user_models
from treasure import models as treasure_models
from .serializers import UserSerializer
import json
# from firebase_admin import messaging
#serialize를 한다는 것은 json이나 xml 파일 등으로 바꾸어 주는 것.
from firebase_admin import credentials
import firebase_admin

# export GOOGLE_APPLICATION_CREDENTIALS= "/home/ubuntu/project3/treasurehunt/treasure-hunt-d0c8c-firebase-adminsdk-vy0uh-88214ea224.json"
# if not firebase_admin._apps:
#     cred = credentials.Certificate('path/to/serviceAccountKey.json') 
#     default_app = firebase_admin.initialize_app(cred)
cred = credentials.Certificate('/home/ubuntu/project3/treasurehunt/treasure-hunt-d0c8c-firebase-adminsdk-vy0uh-88214ea224.json')
firebase_admin.initialize_app(cred)

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

# test
        # send_to_token(token)

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



# messaging test
# def send_to_token(registration_token):
#     # See documentation on defining a message payload.
#     message = messaging.Message(
#         data={
#             'score': '850',
#             'time': '2:45',
#         },
#         token=registration_token,
#     )

#     # Send a message to the device corresponding to the provided
#     # registration token.
#     response = messaging.send(message)
#     # Response is a message ID string.
#     print('Successfully sent message:', response)
