from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rating import rate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

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
            # return Response("something went wrong")


class Login(APIView):
  
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            # return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class Logout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RateView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
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

class getReview(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        reviews=Review.objects.all()
        reviews=ReviewSerializer(reviews,many=True)
        return Response(reviews.data)
    
    def post(self,request):
        print(request.data)
        name=request.data['name']
        product=request.data['product']
        review=request.data['review']
        email=request.data['email']
        date=request.data['date']
        print(name,email,date,product)
        rating=rate(review)
        request.data['rating'] = rating
      
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("saving")
            serializer.save()
        return Response(serializer.data)