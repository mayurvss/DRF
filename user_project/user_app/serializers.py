from rest_framework import serializers
from .models import UserRegister,UserRole

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserRole
        fields='__all__'

class UserRoleSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRole 
        fields=['roll']
        
class UserRegisterSerializer(serializers.ModelSerializer):
    user_role=UserRoleSimpleSerializer(many=True, read_only=True)
    class Meta:
        model =UserRegister
        fields=['name','email_id', 'mobile_no', 'address','user_role']
        
    def to_representation(self, instance):
        print('instance', instance)
        representation = super().to_representation(instance)
        print('representation', representation)
        # Combine roles into a single object
        combined_roles = {"roll": [role["roll"] for role in representation["user_role"]]}
        print(combined_roles)
        # Update the representation
        representation["user_role"] = combined_roles

        return representation
    # def create(self, validated_data):
    #     user_role_data = validated_data.pop('user_role')
    #     user_instance = UserRegister.objects.create(**validated_data)

    #     for role_data in user_role_data:
    #         UserRole.objects.create(user=user_instance, **role_data)

    #     return user_instance
        
