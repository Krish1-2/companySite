from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import *
from .serializer import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView

class Register(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        User = get_user_model()
        try:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class RateView(APIView):
    # item='Pipes'
    def post(self,request):
        print(request.data)
        item=request.data['item']
        print(item)
        return Response(item)
    
    def get(self,request):
        item=request.query_params.get('item')
        print(item)
        # item='Pipes'
        if(item=='pipes'):
            rate=Pipes.objects.all()
            rate=pipeSerializer(rate,many=True)
            print(rate.data)
            return Response(rate.data) 
               
        elif(item=='electricals'):
            rate=Electricals.objects.all()
            rate=electricalsSerializer(rate,many=True)
            print(rate.data)
            return Response(rate.data)
        
        elif(item=='cables'):
            rate=Cables.objects.all()
            rate=cableSerializer(rate,many=True)
            print(rate.data)
            return Response(rate.data)
        
        elif(item=='accessories'):
            rate=Accessories.objects.all()
            rate=accessoriesSerializer(rate,many=True)
            print(rate.data)
            return Response(rate.data)
        
        elif(item=='switchGear'):
            rate=SwitchGear.objects.all()
            rate=switchGearSerializer(rate,many=True)
            print(rate.data)
            return Response(rate.data)
    
        elif(item=='FRPPoleBox'):
            rate=FRPPoleBox.objects.all()
            rate=FrpSerializer(rate,many=True)
            print(rate.data)
            return Response(rate.data)
        
        else:
            return Response({'error': 'Invalid item'})
