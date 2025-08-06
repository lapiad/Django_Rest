# serializers.py
from rest_framework import serializers
from .models import Violation
from .models import User

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'is_active']

class ViolationLogAdminView(serializers.ModelSerializer):
    def get(self, request):
        logs = ViolationLog.objects.all()
        serializer = ViolationLogAdminSerializer(logs, many= True)
        return Response(serializer.data)