from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from appapi.models import users
from appapi.serializers import usersSerializer
from django.contrib.auth.hashers import make_password

# ************************************************************************************************
# GET POST PATCH DELETE usage api



class UserRegistrationAPI(APIView):
    def post(self, request):
        user= request.data
        user._mutable = True
        passw=user['password']
        passw=make_password(passw)
        user['password']=passw
        user._mutable = False
        serializer = usersSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            msg={"status":"success","data":serializer.data}
            return Response(msg,status=status.HTTP_200_OK)
        else:
            msg={"status":"error","data":serializer.errors}
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
 
class UserManagemenetAPI(APIView):
    permission_classes = (IsAuthenticated, )   
    def get(self,request,id=None):
        if id:
            selected_user=users.objects.get(id=id)
            serializer=usersSerializer(selected_user)
            msg={"status":"success","data":serializer.data}
            return Response(msg,status=status.HTTP_200_OK)
# for getting many together
        # selected_user=users.objects.all()
        # serializer=usersSerializer(selected_user,many=True)
        # msg={"status":"success","data":serializer.data}
        # return Response(msg,status=status.HTTP_200_OK)
    
    def patch(self,request,id=None):
            selected_user=users.objects.get(id=id)
            user=request.data
            if user.get('password') is not None:
                user._mutable = True
                passw=user['password']
                passw=make_password(passw)
                user['password']=passw
                user._mutable = False                
            serializer=usersSerializer(selected_user,data=user,partial=True)
            if serializer.is_valid():
             serializer.save()
             msg={"status":"success","data":serializer.data}
             return Response(msg,status=status.HTTP_200_OK)
            else:
             msg={"status":"error","data":serializer.errors}
             return Response(msg,status=status.HTTP_400_BAD_REQUEST)
         
    def delete(self,request,id=None):
            selected_user=get_object_or_404(users,id=id)
            selected_user.delete()
            msg={"status":"success","data":"user deleted"}
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
