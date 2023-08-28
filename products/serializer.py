from rest_framework import serializers
from .models import *


class pipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pipes
		fields =['brand','desc','size','rate']

class cableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cables
		fields =['brand','desc','size','rate']

class switchGearSerializer(serializers.ModelSerializer):
	class Meta:
		model = SwitchGear
		fields =['brand','desc','size','rate']
	
class FrpSerializer(serializers.ModelSerializer):
	class Meta:
		model = FRPPoleBox
		fields =['brand','desc','size','rate']

class accessoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Accessories
		fields =['brand','desc','size','rate']

class electricalsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Electricals
		fields =['brand','desc','size','rate']