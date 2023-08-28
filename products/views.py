from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

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
