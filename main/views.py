from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .models import Activity_peroid
from .serializers import UserSerializer
from .serializers import Activity_peroidSerializer

import json

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
        count = 0;
        for user in users:
            act_arr = []
            count = 0;
            user_dict = { }
            user_dict['id'] = user.id
            user_dict['name'] = user.name
            user_dict['tz'] = user.tz
            for act in acti_pe:
                if(user.id == act.user_id):
                    count = count + 1;
                    # res.append({id: user.id, name: user.name, tz: user.tz, activity_period: {startTime: act.startTime, endTime: act.endTime}})
                    act_dict = {}
                    act_dict['startTime'] = str(act.startTime)
                    act_dict['endTime'] = str(act.endTime)
                    act_arr.append(act_dict)
            user_dict['activity_peroid'] = act_arr
            print("============================")
            print(count)
            res.append(user_dict)

        res = json.dumps(res)
        res = json.loads(res)

        return Response(res)

    def post(self):
        pass


