from rest_framework import serializers
from . import models as user_models

# serializer: 응답으로 보낼 데이터의 형태를 정해주는 하나의 틀
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = "__all__"