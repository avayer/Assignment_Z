from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .models import Activity_peroid
from .serializers import UserSerializer
from .serializers import Activity_peroidSerializer

class userList(APIView):

    def get(self, second_param):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) 
        acti_pe = Activity_peroid.objects.all()
        users = (users)
        acti_pe = (acti_pe)

        # for user in users:
        #     print('id: {}    name: {}    tz: {} '.format(user.id, user.name, user.tz))
        
        # for act in acti_pe:
        #     print('id: {}    startTime: {}     endTime: {} '.format(act.id, act.startTime, act.endTime))

        res = []

        for user in users:
            user_dict = { }
            user_dict.id = user.id
            user_dict.tz = user.tz
            for act in acti_pe:
                if(user.id == act.id):
                    # res.append({id: user.id, name: user.name, tz: user.tz, activity_period: {startTime: act.startTime, endTime: act.endTime}})
                    act_dict = {'startTime': 1, 'endTime': 1}
                    act_dict.startTime = act.startTime
                    act_dict.endTime = act.endTime
                    user_dict.activity_period = (act_dict)
            res.append(user_dict)

        print(res)


        return Response(serializer.data)

    def post(self):
        pass


