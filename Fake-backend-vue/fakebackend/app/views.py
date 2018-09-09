from django.shortcuts import render

"""
views for organising business logic
"""
from typing import Dict, Any
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustumerSerializer


class CustomerView(APIView):
    """
    Get or post a contact instance.
    """

    def get(self, request: Any) -> Response:
        """
        :param request:
        :return:
        """
        contact = Customer.objects.all()
        serializer = CustumerSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request: Any) -> Response:
        """
        :param request:
        :return:
        """
        serializer = CustumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"serializer.data": 200, "status": status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
     Update or delete a contact instance.
    """

    def get_object(self, id: Any) -> Any:
        """
        :param id:
        :return:
        """
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request: Any, id, format=None) -> Response:
        customer = self.get_object(id)
        serializer = CustumerSerializer(customer)
        return Response(serializer.data)

    def put(self, request: Any, id: Any) -> Response:
        """
        :param request:
        :param id:
        :return:
        """
        contact = self.get_object(id)
        serializer = CustumerSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Any, id: Any) -> Response:
        """
        :param request:
        :param id:
        :return:
        """
        contact = self.get_object(id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
