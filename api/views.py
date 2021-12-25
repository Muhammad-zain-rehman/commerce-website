from django.shortcuts import render
from .models import *
from api.serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, authentication


# Create your views here.

class CategoryApiViewPublic(APIView):
    def GET(self, request):
        category_data = Category.objects.all()
        serializer = CategorySerializer(category_data, many=True)
        return Response({
            "success": True, "code": "200", "payload": serializer.data,
            "description": "Category Listing"},
            status=status.HTTP_200_OK)


class CategoryApiView(APIView):

    permission_classes = [permissions.IsAdminUser]

    def POST(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True, "code": "200", "payload": serializer.data,
                "description": "Category Added"},
                status=status.HTTP_200_OK)
        else:
            return Response({
                "success": False, "code": "400", "payload": " ",
                "description": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST)

    def PUT(self, request, pk):
        id1 = pk
        try:
            category_record = Category.objects.get(id=id1)
            serializer = CategorySerializer(category_record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True, "code": "200", "payload": serializer.data,
                    "description": "Record Update"},
                    status=status.HTTP_200_OK)

            return Response({"success": False, "code": "400", "payLoad": " ",
                             "description": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({"success": False, "status": "404", "code": "", "payLoad": "",
                             "description": "you are passing invalid Object which does not exist for update"},
                            status=status.HTTP_404_NOT_FOUND)

    def PATCH(self, request, pk):
        id1 = pk
        try:
            category_record = Category.objects.get(id=id1)
            serializer = CategorySerializer(category_record, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True, "code": "200", "payload": serializer.data,
                    "description": "Record Update"},
                    status=status.HTTP_200_OK)

            return Response({"success": False, "code": "400", "payLoad": " ",
                             "description": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({"success": False, "status": "404", "code": "", "payLoad": "",
                             "description": "you are passing invalid Object which does not exist for update"},
                            status=status.HTTP_404_NOT_FOUND)


class ProductApiViewPublic(APIView):
    def GET(self, request):
        product_data = Product.objects.all()
        serializer = ProductSerializer(product_data, many=True)

        return Response({
            "success": True, "code": "200", "payload": serializer.data,
            "description": "Product Listing"},
            status=status.HTTP_200_OK)


class ProductApiView(APIView):
    def POST(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True, "code": "200", "payload": serializer.data,
                "description": "Product Added"},
                status=status.HTTP_200_OK)
        else:
            return Response({
                "success": False, "code": "400", "payload": " ",
                "description": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST)

    def PUT(self, request, pk):
        id1 = pk
        try:
            product_record = Product.objects.get(id=id1)
            serializer = ProductSerializer(product_record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True, "code": "200", "payload": serializer.data,
                    "description": "Record Update"},
                    status=status.HTTP_200_OK)

            return Response({"success": False, "code": "400", "payLoad": " ",
                             "description": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"success": False, "status": "404", "code": "", "payLoad": "",
                             "description": "you are passing invalid Object which does not exist for update"},
                            status=status.HTTP_404_NOT_FOUND)

    def PUT(self, request, pk):
        id1 = pk
        try:
            product_record = Product.objects.get(id=id1)
            serializer = ProductSerializer(product_record, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True, "code": "200", "payload": serializer.data,
                    "description": "Record Update"},
                    status=status.HTTP_200_OK)

            return Response({"success": False, "code": "400", "payLoad": " ",
                             "description": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"success": False, "status": "404", "code": "", "payLoad": "",
                             "description": "you are passing invalid Object which does not exist for update"},
                            status=status.HTTP_404_NOT_FOUND)



