from rest_framework import serializers
from UserData.models import UserData,UserProblem

#create serializers here

class UserSerializers(serializers.HyperlinkedModelSerializer):
    user_id=serializers.ReadOnlyField()
    class Meta:
        model=UserData
        fields="__all__"

class UserProblemserializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=UserProblem
        fields="__all__"