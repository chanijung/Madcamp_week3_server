from django.db import models
from django.contrib.auth.models import User
from users import models as user_models


class Treasure(models.Model):
    hider = models.ForeignKey("users.User",on_delete=models.CASCADE, related_name = "treasure")
    latitude = models.FloatField()
    longitude = models.FloatField()
    seeker = models.CharField(max_length=50,blank=True, null=True)
    timeSought = models.CharField(max_length=30, blank=True, null=True) 
    # cascade 는 참조된 object가 삭제되면, 이 object를 참조하는 object들도 다 삭제하는거
    # def __str__(self):
    #     return (String)hider.name + "'s treasure at " + String(latitude) +", " String(longitude)
    def serialize_custom(self):
        data = {
            "latitude" : self.latitude,
            "longitude": self.longitude,
            "timeSought": self.timeSought,
        }
        return data

#Contact.objects.filter(id = 1) -> 이미 조건에 해당하는 데이터를 모두 찾아준다.