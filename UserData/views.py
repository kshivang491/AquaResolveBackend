from django.shortcuts import render
from rest_framework import viewsets
from UserData.models import UserData,UserProblem
from UserData.serializers import UserSerializers, UserProblemserializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerializers

    @action(detail=True,methods=['get'])
    def problems(self,request,pk=None):
        try:
            user=UserData.objects.get(pk=pk)
            problems=UserProblem.objects.filter(user=user)
            problems_serializer=UserProblemserializers(problems,many=True,context={'request':request})
            return Response(problems_serializer.data)
        except Exception as e:
            return Response({
                'message':'User might not exists!!'
            })

class UserProblemViewSet(viewsets.ModelViewSet):
    queryset = UserProblem.objects.all()
    serializer_class = UserProblemserializers