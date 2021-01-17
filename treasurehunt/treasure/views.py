from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from users import models as user_models
from . import models as treasures
from firebase_admin import messaging
#serialize를 한다는 것은 json이나 xml 파일 등으로 바꾸어 주는 것.

@csrf_exempt
@api_view(["POST"])
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

# 36.37432 127.36557 n1
# 36.37412 127.36538 twosome

@csrf_exempt
@api_view(["POST"])
def hunt(request):
    if request.method == "POST":
        print("hunt post")
        data_json = json.loads(request.body)
        token = data_json["token"]
        latitude = float(data_json["latitude"])
        longitude =  float(data_json["longitude"])
        print("request latitude: ", latitude)
        print("request longitude: ", longitude)
        treasure_set = treasures.Treasure.objects.all()
        # The `iterator()` method ensures only a few rows are fetched from
        # the database at a time, saving memory.
        print("Iterate through treasure set\n---------------")
        for treasure in treasure_set:
            print(treasure.hider.uid)
            print(treasure.latitude)
            print(treasure.longitude)
            if abs(float(treasure.latitude)-latitude)<0.0001 and abs(float(treasure.longitude)-longitude)<0.0001:
                print("In")
                print("----------------")
                send_to_token(token)
            else:
                print("Out")
                print("----------------")
                
        return Response("hunt post")

# messaging test
def send_to_token(registration_token):
    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'title': 'Treasure Hunt',
            'message': 'You are close to a treasure!',
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)