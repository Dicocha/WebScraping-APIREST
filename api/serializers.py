from rest_framework import serializers
from .models import Vault

class VaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vault
        fields = '__all__'

class TestVaultSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    purpose = serializers.CharField(max_length=999)
    additional_details = serializers.CharField(max_length=999)
    title = serializers.CharField(max_length=255)

    def validate_name(self, value):
        # Add any custom validations as needed

        if "Vault" not in value:
            raise serializers.ValidationError("El nombre de un vault debe de tener la palabra 'Vault' al principio")

        return value
    
    def validate_location(self, value):
        return value
    
    def validate_purpose(self, value):
        return value
    
    def validate_additional_details(self, value):
        return value
    
    def validate_title(self, value):
        return value

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location')
        # *** 
        instance.save()
        return instance
    
    '''
    def save():
    
        It used to logic after validations, for example.
        Is overwrite.
    '''
    