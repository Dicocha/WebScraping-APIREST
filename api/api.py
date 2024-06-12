from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vault
from .serializers import VaultSerializer, TestVaultSerializer

'''
    For add status code in Response add status.Name of code status
    Link: https://www.django-rest-framework.org/api-guide/status-codes/
'''

class VaultViewSet(APIView):

    def get(self, request):
        queryset = Vault.objects.all()
        vault_serializer = TestVaultSerializer(queryset, many = True)

        return Response(vault_serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        vault_serializar = TestVaultSerializer(data = request.data)

        if vault_serializar.is_valid():

            vault_serializar.save()
            return Response(vault_serializar.data)
        
        else:
            return Response(vault_serializar.errors)

class VaultDetails(APIView):
    
    def get(self, request, pk = None):
        queryset = Vault.objects.filter(id = pk).first()
        vault_serializer = TestVaultSerializer(queryset)
        return Response(vault_serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk = None):
        queryset = Vault.objects.filter(id = pk).first()
        vault_serializer = TestVaultSerializer(queryset, data=request.data)
        if vault_serializer.is_valid():
            vault_serializer.save()
            return Response(vault_serializer.data, status= status.HTTP_200_OK)
        return Response(vault_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk = None):
        queryset = Vault.objects.filter(id = pk).first()
        queryset.delete()
        return Response({'message':'Vault eliminado'}, status=status.HTTP_200_OK)