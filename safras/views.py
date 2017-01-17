from django.shortcuts import get_object_or_404

from m2agro.permissions import IsAuthenticatedOrReadOnly

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from safras.models import Safra
from safras.serializers import SafraSerializer


class SafrasList(APIView):
    """
    List all, or create a new one.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
    # Podemos realizar filtos no resultado de safras
        safras = Safra.objects.filter(is_active=True)
        serializer = SafraSerializer(safras, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SafraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SafraDetail(APIView):
    """
    Retrieve, update or delete a instance.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        return get_object_or_404(Safra, pk=pk)

    def get(self, request, pk, format=None):
        safra = self.get_object(pk)
        serializer = SafraSerializer(safra)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        safra = self.get_object(pk)
        serializer = SafraSerializer(safra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        safra = self.get_object(pk)
        safra.delete()
        return Response(safra)